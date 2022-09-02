from flask import jsonify

from ...main import app
from ...core.ext import db


@app.route('/')
def root():
   return 'Hello world!'


@app.route('/drop', methods=['GET'])
def drop_all_tables():
   db.drop_all()

   return jsonify('all drop!')

