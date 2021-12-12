from flask import Flask
from flask import jsonify
from flask import request
from flask import session

"""
request.method：获取客户端请求的方法
request.header：获取请求头
request.cookies：获取cookie
request.args：获取get请求提交的数据
request.form：获取post请求提交的数据
request.values：获取post或者get请求提交的数据
"""
from flask import render_template  # 导入模块，返回html文件
from flask import make_response

"""
make_response()：创建response对象
set_cookie(key,value,max_age)：设置cookie
request.cookies.get(key)：获取cookie
request.delete_cookie(key)：删除cookie
"""

# 创建对象
app = Flask(__name__)
# 使jsonify的返回值不显示乱码，直接显示中文字符串
app.config['JSON_AS_ASCII'] = False
# 实现客户端的session会话保持，先设置秘钥:用于session信息加密
app.secret_key = "lhl19940618"

users_info = {'1001': ['123456', '张三', 9000],
              '1002': ['123456', '李四', 9000],
              '1003': ['123456', '王五', 9000],
              '1004': ['123456', '赵六', 9000]}


# 编写静态路由，构建url与函数的映射关系（将函数与url绑定）
@app.route('/users', methods=["get"])
def users():
    return jsonify({"code": 10000, "message": "success", "data": users_info})


# 动态路由（可获取不同的数据结果）：访问url中不同的资源路径
# 不同资源路径的常见格式：<数据类型：变量名>
# @app.route('/users/<string:account>', methods=["get"])

# 通过传入不同的请求参数，返回不同的json数据。
@app.route('/users/acc', methods=["get"])
def get_user():
    # 获取cookie中指定键的值
    # get_cookie = request.cookies.get("username")
    # 获取session中指定键的值
    get_session = session.get('acc')
    # 获取客户端请求的参数account的值
    res = request.args.get("account")
    if get_session:
        if res:  # 检查请求参数是否正确
            if res in users_info:
                info = users_info[res]
                return jsonify({"code": 10000, "message": "success", "data": {"name": info[1], "balance": info[2]}})
            else:
                return jsonify({"code": 10001, "message": "account is not exist "})
        else:
            return jsonify({"code": 10002, "message": "param error "})
    else:
        return jsonify({"code": 10003, "message": "请先登录系统"})


# post方法请求需要有请求体,单纯通过游览器发送URL无法成功
@app.route('/login', methods=["post"])
def login():
    # post方法请求时，获取from数据类型的方式
    # res_ac = request.form.get("account")

    # 获取客户端请求的参数account的值
    res_ac = request.values.get("account")
    res_pw = request.values.get("password")
    if res_ac and res_pw:  # 检查请求参数是否正确
        if res_ac in users_info:  # 检查账号是否存在
            info = users_info[res_ac]
            if res_pw == info[0]:  # 检查密码是否正确
                res = make_response(jsonify({"code": 10000, "message": "success"}))
                # 登录成功后将用户信息保存到cookie
                # res.set_cookie('username', res_ac, max_age=60)
                # 添加session
                session['acc'] = res_ac
                return res
            else:
                return jsonify({"code": 10003, "message": "password error"})
        else:
            return jsonify({"code": 10002, "message": "account is not exist "})
    else:
        return jsonify({"code": 10001, "message": "param error "})


@app.route('/logout', methods=["delete"])
def logout():
    try:
        rest = request.args.get("account")
        res = make_response({"id": rest, "code": 10000, "message": "logout success"})
        # 删除指定cookie
        # res.delete_cookie('acc')
        session.pop('acc')
        return res
    except Exception:
        return jsonify({"code": 10001, "message": "unknown error"})


if __name__ == "__main__":
    # 使用默认方式启动项目
    # app.run()
    # 以调试模式启动项目
    # .. host='0.0.0.0' 表示可使用127.0.0.1、localhost、192.168.1.5
    app.run(host='0.0.0.0', port=5000, debug=True)
