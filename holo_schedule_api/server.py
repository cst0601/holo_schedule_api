from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

from holo_schedule_api.web_service import WebService
from holo_schedule_api.twitter_service import TwitterService

import logging

app = Flask(__name__)
CORS(app)

WebService.register(app, route_base="/")
TwitterService.register(app, route_base="/")

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("server")
logger.warning("Server starting...")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)