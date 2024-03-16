from flask import Flask
from werkzeug.routing.converters import BaseConverter  # 导入自定义类型支持模块

app = Flask(__name__)

#   配置加载项方式一
# config = {
#     'DEBUG': True
# }
#
# app.config.update(config)

#   配置加载项方式二
app.config["DEBUG"] = True


#   创建基于自定义类型实现类
class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


#   把自定义类型注册到路由中
app.url_map.converters['mob'] = MobileConverter


#   基于自定义类型结合正则完成一个具有手机号校验的参数传递路由
@app.route("/sms/<mob:mobile>")
def sms(mobile):
    return f"Hello, {mobile}"


#   默认首页
@app.route("/")
def hello_world():
    return "hello"


if __name__ == "__main__":
    app.run()
