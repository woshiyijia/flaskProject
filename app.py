# 从flask中导入Flask类
from flask import Flask, render_template

# 使用Flask类创建一个app对象
# Flask类构造函数参数__name__代表app.py这个模块
# 1.以后出现bug可以帮助我们，快速定位
# 2.对于寻找模块文件，有一个相对路径
app = Flask(__name__)


# # 创建一个路由和视图函数的映射
# # Flask类的route()函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。
# # app.route(rule, options) rule：表示与该函数的URL绑定 options： 是要转发给基础Rule对象的参数列表 这里的'/'就是与函数hello_world()函数绑定
# @app.route('/admin')
# def admin():
#     return 'Hello Admin!'
#
#
# @app.route("/guest/<guest>")
# def guest(guest):
#     return "Hello Guest！"+guest
#
#
# @app.route("/user_login/<name>")
# def log(name):
#     match name:
#         case "admin":
#             return redirect(url_for("admin"))
#         case "guest":
#             return redirect(url_for("guest", guest=name))
#         case _:
#             return "url不正确！！"
#
# @app.route("/login/",methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         print(1)
#         user = request.form['nm'] # 获取表单数据
#         return redirect(url_for('success', name=user))
#     else:
#         print(2)
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=user))
#
# @app.route('/')
# def index():
#     return render_template("login.html")
#
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name

# @app.route("/")
# def index():
#     my_str = "水果"
#     my_int = 80
#     my_source = "云南"
#     my_array = [my_str, my_int, my_source]
#     my_dict = {
#         "cate": my_str,
#         "price": my_int,
#         "source": my_source,
#         "array": my_array
#     }
#     return render_template("things.html",
#                            my_str=my_str,
#                            my_int=my_int,
#                            my_source=my_source,
#                            my_array=my_array,
#                            my_dict=my_dict
#                            )

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # Flask类的run()方法在本地开发服务器上运行应用程序
    app.run()
