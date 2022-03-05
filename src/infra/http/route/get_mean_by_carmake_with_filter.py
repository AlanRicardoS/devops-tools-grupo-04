from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.get_mean_by_carmake_with_filter as get_mean_by_carmake_with_filter
import flask


def route(app: flask.app.Flask):
    @app.route('/carmake/filter', methods=['GET'])
    @auth.requires_auth
    def request_get_example():
        try:

            response = get_mean_by_carmake_with_filter.get_mean_by_carmake_with_filter(
                request.headers["carmake"])

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
