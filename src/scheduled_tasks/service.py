from datetime import datetime
from typing import Union
from scheduled_tasks.model import ScheduledAggregation, ScheduledCheck
from scheduled_tasks.persistence import ScheduledTasksPersistence
from utils import interval_filter


class ScheduledTasksService():
    def __init__(self, tasks_persistence: ScheduledTasksPersistence):
        self._tasks = tasks_persistence

    def get_all_tasks_for_datetime(self, selected_datetime: datetime) -> list[Union[ScheduledCheck, ScheduledAggregation]]:
        frequencies = interval_filter.get_divisible_frequencies(
            selected_datetime)
        day_filters = interval_filter.get_day_filters(selected_datetime)

        tasks = []
        for frequency in frequencies:
            for day_filter in day_filters:
                tasks.extend(self._tasks.get_scheduled_tasks(
                    frequency, day_filter))

        return tasks
