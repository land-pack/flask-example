class BaseConfig(object):
    DEBUG = False
    # PORT = 6000
    SERVER_NAME = '0.0.0.0:6000'
    # HOST = '0.0.0.0'


class DevConfig(BaseConfig):
    pass


config = {
    "base": BaseConfig,
    "dev": DevConfig
}
