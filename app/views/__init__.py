from flask import Blueprint
from flask_restful import Api
api_bp = Blueprint('api_1_0', __name__)
api = Api(api_bp)


# 导入视图

from . import taskview1,taskview2