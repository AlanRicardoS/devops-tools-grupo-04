from flask import jsonify
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.get_mean_by_carmake as carmake
import flask


def route(app: flask.app.Flask):
    @app.route('/car_make', methods=['GET'])
    @auth.requires_auth
    def request_get_carmake():
        try:
            response = carmake.get_mean_by_carmake()

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500

    
