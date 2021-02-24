

class Config:
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://s200:123321@192.168.31.66:3306/flask_app"
    SQLALCHEMY_TRACK_MODIFICATIONS=True 

    # redis 配置
    REDIS_HOST='192.168.31.66'
    REDIS_PORT='6379'

    pass

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_map={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}