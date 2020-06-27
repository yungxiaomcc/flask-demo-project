from flask import Blueprint
from flask_restful import Api
api_bp = Blueprint('api_1_1', __name__)
api = Api(api_bp)


# 导入视图
from . import test