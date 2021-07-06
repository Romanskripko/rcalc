import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aCTyvBh2Ix-l0dd1gMWR1g'
    UPLOAD_FOLDER = os.path.join(app_dir, 'app', 'tables')
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000
    ALLOWED_EXTENSIONS = {'xlsx'}


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
