from app.models import BaseModel
from app import db

class ImageUrlInfo(db.Model):
    __tablename__ = 't_ImageUrlInfo'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(3000))
    object_name = db.Column(db.String(100), nullable=False)  # 图片url 对应的对象
    