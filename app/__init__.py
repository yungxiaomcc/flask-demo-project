from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import CORS
from flask_session import Session
from config import config_map
pymysql.install_as_MySQLdb()


db = SQLAlchemy()
redis_store = None
config_class = None

# 配置日志
logging.basicConfig(level=logging.ERROR)
# 创建日志记录器，指明日志保存的路径，没个日志文件的最大大小，保存的日志文件个数上限
file_log_handler = RotatingFileHandler('logs/log',maxBytes=1024*1024*100, backupCount=10)
# 日志记录格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    global config_class
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    db.init_app(app)
    global redis_store

    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST,port=config_class.REDIS_PORT)

    # flask session 配置
    Session(app)
    app.url_map.converters['re'] = ReConvert

    # 注册蓝图
    from app.views import api_bp
    app.register_blueprint(api_bp)
    return app

    
