from operator import ge
from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import flask
from src.infra.utility.generator import Generator


def route(app: flask.app.Flask):
    @app.route('/file', methods=['POST'])
    @auth.requires_auth
    def request_post_example():
        try:
            dataset = request.files["dataset"]
            name = Generator.radom_string_number()
            date = Generator.date_now_isoformat()
            file = "files/datasets/"+date + "_" + name + ".csv"
            dataset.save(file)
            return jsonify(), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
