import requests
import pytest
from bs4 import BeautifulSoup

from holo_schedule_api.service.crawler import Crawler
from holo_schedule_api.service.date_schedule import DateSchedule


@pytest.fixture
def container_soup():
    containers = None
    with open("tests/schedule_all_raw.html", "r") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
        containers = soup.find("div", class_="tab-pane show active").find_all(
            "div", class_="container", recursive=False)
    return containers


@pytest.fixture
def schedule_soup():
    schedule = None
    with open("tests/schedule_raw.html", "r") as file:
        schedule = BeautifulSoup(file.read(), "html.parser")
    return schedule


class TestCrawler:
    def setup_class(self):
        self.crawler = Crawler()

    def teardown_method(self):
        pass

    def test_get_date_schedules(self, container_soup):
        date_schedules = self.crawler.get_date_schedules(container_soup)

        assert 3 == len(date_schedules)
        assert "08/26" == date_schedules[0].date
        assert "08/27" == date_schedules[1].date
        assert "08/28" == date_schedules[2].date
        assert "天音かなた" == date_schedules[0].schedules[0].member
        assert "00:00" == date_schedules[0].schedules[0].time
        assert "猫又おかゆ" == date_schedules[2].schedules[0].member

    def test_get_date_tags(self, container_soup):
        container_tags = self.crawler.get_date_tags(container_soup)

        assert 0 == container_tags[0][0]
        assert 4 == container_tags[1][0]
        assert 16 == container_tags[2][0]
        assert "08/26" == container_tags[0][1]
        assert "08/27" == container_tags[1][1]
        assert "08/28" == container_tags[2][1]

    def test_generate_schedule(self, schedule_soup):
        schedule = self.crawler.generate_schedule(schedule_soup)

        assert schedule.member == "獅白ぼたん"
        assert schedule.time == "01:59"
        assert schedule.youtube_url == "https://www.youtube.com/watch?v=vgX_7SD8Qts"