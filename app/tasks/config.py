from config import Config

# 设置celery中的代理
BROKER_URL = "redis://{}:{}/5".format(Config.REDIS_HOST, Config.REDIS_PORT)

# 设置异步任务返回结果存放的地址
CELERY_RESULT_BACKEND = 'redis://{}:{}/6'.format(Config.REDIS_HOST, Config.REDIS_PORT)

SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI