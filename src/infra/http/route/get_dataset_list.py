from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.get_dataset_list as get_dataset_list
import flask


def route(app: flask.app.Flask):
    @app.route('/list/dataset', methods=['GET'])
    @auth.requires_auth
    def request_get_dataset_list():
        try:

            response = get_dataset_list.get_dataset_list()

            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
