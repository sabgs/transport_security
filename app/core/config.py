import os

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config():
   DEBUG = False

   DB_HOST = os.environ.get('DATABASE_HOST', 'localhost')
   DB_PORT = os.environ.get('DATABASE_PORT', 5432)
   DB_USER = os.environ.get('DATABASE_USERNAME')
   DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')
   DB_NAME = os.environ.get('DATABASE_NAME')

   SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
   SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
   DEBUG = True
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')


class ProductionConfig(Config):
   pass

config_names = dict(
   dev=DevelopmentConfig,
   prod=ProductionConfig
)