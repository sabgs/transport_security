import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config():
	DEBUG = False


class DevelopmentConfig(Config):
   DEBUG = True

   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
   SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
   SQLALCHEMY_TRACK_MODIFICATIONS = False


config_names = dict(
   dev=DevelopmentConfig,
   prod=ProductionConfig
)