from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class BaseModel(object):
    '''
    模型文件的基类
    '''
    pass

class User(BaseModel,db.Model):
    pass