''' Configuration file for the API '''

class Config(object):
    ''' Parent configutation class '''
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    ''' Configuration for development environment '''
    DEBUG = True

class StagingConfig(Config):
    ''' Configuration for the staging environment '''
    DEBUG = True

class TestingConfig(Config):
    ''' Configuration for the testing environment '''
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    ''' Configuration for the production environment '''
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}