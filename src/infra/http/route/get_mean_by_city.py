from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.get_mean_by_city as get_mean_by_city
import flask


def route(app: flask.app.Flask):
    @app.route('/city', methods=['GET'])
    @auth.requires_auth
    def request_get_city():
        try:

            response = get_mean_by_city.get_mean_by_city()

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
