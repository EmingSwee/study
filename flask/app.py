from flask import Flask
from werkzeug.routing.converters import BaseConverter  # 导入自定义类型支持模块

app = Flask(__name__)


#   基于父类创建一个通用正则类
class RegexeConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]


#   把自定义类型注册到路由中
app.url_map.converters['regex'] = RegexeConverter


#   基于通用自定义类型结合自己可控的正则完成一个具有手机号校验的参数传递路由
@app.route("/sms/<regex('1[3-9]\d{9}'):mobile>")
def sms(mobile):
    return f"Hello, {mobile}"


#   基于通用自定义类型结合自己可控的正则完成一个具有id校验的参数传递路由
@app.route("/goods/<regex('\d+'):id>")
def goods(id):
    return f"Hello, {id}"


#   默认首页
@app.route("/")
def hello_world():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)

#   命令行运行案例 文件名使用app.py 命令行输入flask run 即可
