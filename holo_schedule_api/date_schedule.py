

class DateSchedule:
    """ Schedules of a date
    """
    def __init__(self, date, schedules=None):
        self.date = date
        self.schedules = schedules

    def append(self, schedule):
        self.schedules.append(schedule)