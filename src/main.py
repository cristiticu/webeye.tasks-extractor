from typing import Any, TYPE_CHECKING

from context import ApplicationContext
import settings
if TYPE_CHECKING:
    from aws_lambda_typing.context import Context


application_context = ApplicationContext()


def lambda_handler(event: dict[str, Any], context: "Context") -> dict[str, Any]:
    try:

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


if __name__ == "__main__":
    if settings.ENVIRONMENT == "dev":
        print([o for o in application_context.scheduled_tasks_persistence.get_scheduled_tasks(
            "2m", "all")])
