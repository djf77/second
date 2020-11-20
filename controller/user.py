# controller/user.py

from flask import Blueprint, jsonify
import datebase

user_bp = Blueprint('user', __name__, url_prefix='/user')


# 列出用户信息接口
@user_bp.route('', methods=['GET'])
def show_users_list():
    list_before_fixed = datebase.show_all_users()
    list_fixed = [x[0] for x in list_before_fixed]
    response = jsonify(list_fixed)
    return response
