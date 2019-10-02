import os


class Config:
    ES_HOSTS = os.environ.get('ES_HOSTS')
    LOG_PATH = os.environ.get('LOG_PATH')
    ENV=os.environ.get('ENVIRONMENT')
class DevelopmentConfig(Config):
    maxBytes = 500
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    maxBytes = 1000
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
