from flask import request, jsonify, abort
from flask_classful import FlaskView, route

from searchtweets import load_credentials, gen_request_parameters, collect_results

RESULTS_PER_CALL = 15


class TwitterService(FlaskView):
    def __init__(self):
        self.search_args = load_credentials(
            filename="holo_schedule_api/credentials/credentials.yaml",
            yaml_key="search_tweets_v2",
            env_overwrite=False)

    @route("/twitter/search", methods=["GET"])
    def search(self):
        query = request.args.get("query")
        if query == "" or query is None:
            abort(404)

        request_param = gen_request_parameters(
            query,
            results_per_call=RESULTS_PER_CALL,
            tweet_fields="author_id",
            stringify=False)
        tweets = collect_results(request_param,
                                 max_tweets=RESULTS_PER_CALL,
                                 result_stream_args=self.search_args)
        print(tweets)
        tweets_url = [
            "https://twitter.com/{}/status/{}".format(tweet["author_id"],
                                                      tweet["id"])
            for tweet in tweets[0:RESULTS_PER_CALL]
        ]

        response_json = {}
        response_json["query"] = query
        response_json["newest_id"] = tweets[-1]["newest_id"]
        response_json["tweets_url"] = tweets_url
        return jsonify(response_json), 200