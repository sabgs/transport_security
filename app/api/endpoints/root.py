from flask import request, jsonify
from marshmallow import ValidationError

from ...main import app
from ...core.ext import db


@app.route('/')
def root():
   return '123123'


@app.route('/drop', methods=['GET'])
def test():
   try:
      db.drop_all()
   except ValidationError as err:
      return jsonify(err.messages)

   return jsonify('all drop!')

