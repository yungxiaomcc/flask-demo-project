



class Config:
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:密码@ip地址:端口/annotation"
    SQLALCHEMY_TRACK_MODIFICATIONS=True 

    # redis 配置
    REDIS_HOST=''
    REDIS_PORT=''

    # flask-session
    SESSION_TYPE='redis'
    SECRET_KEY=''
    SESSION_REDIS=redis.StrictRedis(host=REDIS_HOST,PORT=REDIS_PORT,db=1)
    SESSION_USE_SIGNER = True # 对cookie中的session_id 进行隐藏处理
    PERMANENT_SESSION_LIFETIME=86400 # session 有效期
    pass

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

config_map={
    'dev':DevConfig,
    'prod':ProdConfig
}