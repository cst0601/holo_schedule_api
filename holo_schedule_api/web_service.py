from flask import request, jsonify, abort
from flask_classful import FlaskView, route

from holo_schedule_api.service.crawler import Crawler


class WebService(FlaskView):

    def __init__(self):
        self.crawler = Crawler()
        self.region_url = {
            "hololive": "hololive",
            "en": "english",
            "id": "indonesia"
        }

    @route("/schedules", methods=["GET"])
    @route("<string:region_code>/schedules", methods=["GET"])
    def get_schedules(self, region_code=None):
        if region_code == None:
            return jsonify(self.crawler.get_schedules()), 200
        elif self.region_url[region_code] != None:
            return jsonify(
                self.crawler.get_schedules(self.region_url[region_code])), 200

    @route("/schedules/today", methods=["GET"])
    @route("<string:region_code>/schedules/today", methods=["GET"])
    def get_today_schedules(self, region_code=None):
        if region_code == None:
            print("region code unspecified")
            return jsonify(self.crawler.get_today_schedules()), 200
        elif self.region_url[region_code] != None:
            return jsonify(
                self.crawler.get_today_schedules(
                    self.region_url[region_code])), 200