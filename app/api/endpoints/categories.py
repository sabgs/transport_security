from flask import jsonify, request

from ...main import app
from ..servise import categories as service

ENDPOINT_STR = '/categories'

@app.route(f'{ENDPOINT_STR}', methods=['GET'])
def get_all_categories():
   return jsonify(service.get_all())


@app.route(f'{ENDPOINT_STR}', methods=['POST'])
def create_category():
   data = request.get_json()
   return jsonify(service.create(data))


@app.route(f'{ENDPOINT_STR}/<int:number>', methods=['GET'])
def get_category_by_number(number):
   return jsonify(service.get_one_by_number(number))
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])
# @app.route(f'{ENDPOINT_STR}', methods=['GET'])