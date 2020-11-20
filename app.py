# app.py
from flask import Flask, jsonify, request, Blueprint
import datebase
from utils import HttpError

app = Flask(__name__)


# 注册一个错误处理器
@app.errorhandler(HttpError)
def handle_http_error(error):
    response = jsonify(error.to_dict())  # 创建一个Response实例
    response.status_code = error.status_code  # 修改HTTP状态码
    return response


# 添加用户接口
add_bp = Blueprint('add', __name__, url_prefix='/add')


@add_bp.route('', methods=['POST'])
def add_users():
    data = request.get_json(force=True)  # 捕获前端的请求内容
    username = data.get('name')
    student_nums = data.get('num')

    if username is None and student_nums is None:
        raise HttpError(400, '缺少参数 name\n 缺少参数 num')
    if username is None:
        raise HttpError(400, '缺少参数 name')
    if student_nums is None:
        raise HttpError(400, '缺少参数 num')

    datebase.save_add(username, student_nums)

    return '添加成功'


# 列出用户信息接口
users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('')
def show_users_list():
    list_before_fixed = datebase.show_all_users()
    list_fixed = [x[0] for x in list_before_fixed]
    response = jsonify(list_fixed)
    return response


if __name__ == '__main__':
    app.run()
