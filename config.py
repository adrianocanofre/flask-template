import os


class Config:
    DEPENDENCY_API_A_URL = os.environ.get('DEPENDENCY_API_A_URL')
    DEPENDENCY_API_B_URL = os.environ.get('DEPENDENCY_API_B_URL')
    GIT_TAG = os.environ.get('GIT_TAG')
    ES_HOSTS = os.environ.get('ES_HOSTS')
    LOG_PATH = os.environ.get('LOG_PATH')

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
