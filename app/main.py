from flask import Flask

from .core.ext import db
from .core.config import config_names

from .models.category import Category
from .models.question import Question
from .models.answer import Answer


app = Flask(__name__)


@app.before_first_request
def test():
   db.create_all()

def create_app(name: str = 'dev'):
   app.config.from_object(config_names[name])
   db.init_app(app)

   from .api.endpoints import root, categories, questions

   return app