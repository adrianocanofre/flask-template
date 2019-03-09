import os


class Config:
    DEPENDENCY_API_A_URL = os.environ.get('DEPENDENCY_API_A_URL')
    DEPENDENCY_API_B_URL = os.environ.get('DEPENDENCY_API_B_URL')
    GIT_TAG = os.environ.get('GIT_TAG')
    ES_HOSTS = os.environ.get('ES_HOSTS')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
