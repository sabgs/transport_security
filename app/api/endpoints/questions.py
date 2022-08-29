from flask import jsonify, request

from ...main import app
from ..servise import questions as service

ENDPOINT_STR = '/questions'

@app.route(f'{ENDPOINT_STR}', methods=['GET'])
def get_all_questions():
   return jsonify(service.get_all())

@app.route(f'{ENDPOINT_STR}', methods=['POST'])
def create_question():
   data = request.get_json()
   return jsonify(service.create(data))


# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])