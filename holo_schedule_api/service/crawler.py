import requests
import re
from datetime import datetime, timedelta


from bs4 import BeautifulSoup

from holo_schedule_api.service.schedule import Schedule
from holo_schedule_api.service.date_schedule import DateSchedule

URL = "https://schedule.hololive.tv/lives/hololive"


class Crawler:
    def __init__(self):
        self.schedules = self.crawl()
        self.last_update_time = datetime.utcnow()

    def get_schedules(self):
        time_now = datetime.utcnow()
        if (self.last_update_time + timedelta(minutes=5) < time_now):
            self.last_update_time = time_now
            self.schedules = self.crawl()

        schedule_dict = {
            "update_time": 
            self.last_update_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        schedule_dict["schedule"] = [date_schedules.to_dict() for date_schedules in self.schedules]

        return schedule_dict

    def crawl(self):
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        containers = soup.find("div", class_="tab-pane show active"
            ).find_all("div", class_="container", recursive=False)

        return self.get_date_schedules(containers)

    def generate_schedule(self, element):
        """ Generates schedule from beautifulSoup element
        """
        youtube_url = element.find("a", href=True)["href"]
        member = element.find("div", class_="col text-right name").text.strip()
        time = element.find("div", class_="col-5 col-sm-5 col-md-5 text-left datetime").text.strip()
        
        return Schedule(time, member, youtube_url)

    def get_date_tags(self, containers):
        """ Classify streams by date and label with start of container id.
            Returns list of tuples which contains start of container id and date of
            each group.
        """
        date_tags = []

        for i, element in enumerate(containers):
            # special style only exists for time banner
            time_banner = element.find("div", class_="navbar navbar-inverse")

            if time_banner:
                removed_return = re.sub("\r", "", time_banner.div.text) # difference between test and actual web content
                date_tags.append((i, re.sub("\n\s+", "", removed_return)))
        
        return date_tags

    def get_date_schedules(self, containers):
        """ Generates a list of schedules by date (DateSchedule)
        """
        date_schedules = []
        tags = self.get_date_tags(containers)

        for i, tag in enumerate(tags):
            schedules = []
            containers_of_date = containers[
                tag[0]: tags[i+1][0] if i+1 != len(tags) else len(containers)]
            
            for container in containers_of_date:
                schedules.extend([self.generate_schedule(schedule_soup) for schedule_soup in container.find_all(
                    "div", class_="col-6 col-sm-4 col-md-3") if schedule_soup != None])
            
            date_schedules.append(DateSchedule(tag[1], schedules))
        
        return date_schedules
