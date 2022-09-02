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


@app.route(f'{ENDPOINT_STR}/<int:id>', methods=['GET'])
def get_question_by_id(id):
   return jsonify(service.get_single_question(id))
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])