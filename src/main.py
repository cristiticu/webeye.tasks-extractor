from datetime import datetime, timezone
from typing import Any, TYPE_CHECKING

from context import ApplicationContext
import settings
from utils.sqs import send_messages

if TYPE_CHECKING:
    from aws_lambda_typing.context import Context


application_context = ApplicationContext()


def lambda_handler(event: dict[str, Any], context: "Context") -> dict[str, Any]:
    try:
        tasks = application_context.scheduled_tasks.get_all_tasks_for_datetime(
            datetime.now(timezone.utc))

        print(f"Tasks: {tasks}")

        check_tasks = [{"u_guid": str(task.u_guid), "w_guid": str(task.w_guid), "configuration": task.configuration.model_dump(
            mode="json")} for task in tasks if task.task_type == "CHECK"]

        aggregate_tasks = [
            {"u_guid": str(task.u_guid), "configuration": task.configuration.model_dump(
                mode="json")} for task in tasks if task.task_type == "AGGREGATE"]

        if len(check_tasks) > 0:
            send_messages(settings.SQS_CHECK_QUEUE_URL, check_tasks)

        if len(aggregate_tasks) > 0:
            send_messages(settings.SQS_AGGREGATIONS_QUEUE_URL, aggregate_tasks)

        return {
            "statusCode": 200,
            "body": "Completed check",
            "headers": {
                "Content-Type": "application/json"
            }
        }

    except Exception as e:
        print(e)

        return {
            "statusCode": 400,
            "body": "Bad Request. No result",
            "headers": {
                "Content-Type": "application/json"
            }
        }
