from scheduled_tasks.persistence import ScheduledTasksPersistence


class ApplicationContext():
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ApplicationContext, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.scheduled_tasks_persistence = ScheduledTasksPersistence()
