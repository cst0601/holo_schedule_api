from typing import List
from datetime import datetime, timedelta, timezone

from holo_schedule_api.service.date_schedule import DateSchedule


class ScheduleCache:
    """ Cache of Hololive schedule
        region_code is one of the three groups of Hololive: Hololive, EN, ID
    """
    def __init__(self, region_code: str, schedules: List[DateSchedule] = None):
        self.region_code = region_code
        self.schedules = schedules
        self.last_update_time = datetime.utcnow()

    def is_expired(self) -> bool:
        """ if the cache expired (5 mins)
        """
        time_now = datetime.utcnow()
        return True if (
            self.last_update_time + timedelta(minutes=5) < time_now) else False

    def update(self, schedules):
        self.last_update_time = datetime.utcnow()
        self.schedules = schedules

    def get_schedules(self):
        return {
            "region":
            self.region_code,
            "update_time":
            self.last_update_time.strftime("%Y-%m-%d %H:%M:%S"),
            "schedule":
            [date_schedules.to_dict() for date_schedules in self.schedules]
        }