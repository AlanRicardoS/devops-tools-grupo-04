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
            print("1")
            dataset = request.files["dataset"]
            print("1")
            gen = Generator.radom_string_number()
            print(gen)
            dataset.save("files/datasets/"+gen+".csv")
            return jsonify(), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
