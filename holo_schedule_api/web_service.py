from flask import request, jsonify
from flask_classful import FlaskView, route

from holo_schedule_api.service.crawler import Crawler

class WebService(FlaskView):
    def __init__(self):
        self.crawler = Crawler()

    @route("/schedules", methods=["GET"])
    def get_schedules(self):
        return jsonify(self.crawler.get_schedules()), 200