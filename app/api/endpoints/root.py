from flask import request, jsonify
from marshmallow import ValidationError

from ...main import app
from ...schemas.request_data import RequestSchema

@app.route('/')
def root():
   return '123123'


@app.route('/test', methods=['POST'])
def test():
   try:
      data = request.get_json()['questions']
      num = request.get_json()['category']
      print(num)
      rs = RequestSchema(many=True)
      res = rs.load(data)
   except ValidationError as err:
      return jsonify(err.messages)

   return jsonify(rs.dump(res))

