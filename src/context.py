from scheduled_tasks.persistence import ScheduledTasksPersistence
from scheduled_tasks.service import ScheduledTasksService


class ApplicationContext():
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ApplicationContext, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.scheduled_tasks_persistence = ScheduledTasksPersistence()
        self.scheduled_tasks = ScheduledTasksService(
            self.scheduled_tasks_persistence)
