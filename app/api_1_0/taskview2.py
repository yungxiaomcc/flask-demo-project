from flask import jsonify

from . import api_bp, api
from app.models import user


@api_bp.route("/user/test")
def test():
    return jsonify(retCode=0, des='success',ver='version 1.0')