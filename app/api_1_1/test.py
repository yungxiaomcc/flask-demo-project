from flask import jsonify
from . import api_bp

@api_bp.route("/user/test")
def test():
    return jsonify(retCode=0, des='success', ver='version 1.1')