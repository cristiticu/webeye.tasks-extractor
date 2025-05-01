from typing import Union
from scheduled_tasks.model import ScheduledAggregation, ScheduledCheck, ScheduledTask
import settings
from boto3.dynamodb.conditions import Key
from utils.dynamodb import dynamodb_table


class ScheduledTasksPersistence():
    def __init__(self):
        self.tasks = dynamodb_table(
            settings.SCHEDULED_TASKS_TABLE_NAME, settings.SCHEDULED_TASKS_TABLE_REGION)

    def get_scheduled_tasks(self, frequency: str, day_filter: str) -> list[Union[ScheduledCheck, ScheduledAggregation]]:
        schedule = f"{frequency}#{day_filter}"

        response = self.tasks.query(
            IndexName=settings.SCHEDULED_TASKS_SCHEDULE_GSI,
            KeyConditionExpression=Key("schedule").eq(schedule)
        )
        items = response.get("Items")

        return [ScheduledTask.from_db_item(item) for item in items]
