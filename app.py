# app.py
from flask import Flask, jsonify
from utils import HttpError
from controller.add import add_bp
from controller.user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(add_bp)


# 注册一个错误处理器
@app.errorhandler(HttpError)
def handle_http_error(error):
    response = jsonify(error.to_dict())  # 创建一个Response实例
    response.status_code = error.status_code  # 修改HTTP状态码
    return response


if __name__ == '__main__':
    app.run(debug=True)
