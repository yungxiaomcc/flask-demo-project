from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class BaseModel(object):
    '''
    模型文件的基类
    '''
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


from . import user, video, image
