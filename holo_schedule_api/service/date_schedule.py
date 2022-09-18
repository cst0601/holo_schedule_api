class DateSchedule:
    """ Schedules of a date
    """

    def __init__(self, date, schedules=None):
        self.date = date
        self.schedules = schedules

    def append(self, schedule):
        self.schedules.append(schedule)

    def to_dict(self):
        return {
            "date":
            self.date,
            "schedules": [
                schedule.to_dict() for schedule in self.schedules
                if self.schedules != None
            ]
        }
