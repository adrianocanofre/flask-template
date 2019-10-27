import os


class Config:
    ES_HOSTS = os.environ.get('ES_HOSTS')

    ENV=os.environ.get('ENVIRONMENT')
class DevelopmentConfig(Config):
    maxBytes = 500
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    LOG_PATH = os.environ.get('LOG_PATH')


class ProductionConfig(Config):
    maxBytes = 1000
    DEBUG = False
    LOG_PATH = os.environ.get('LOG_PATH') or 'log/'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
