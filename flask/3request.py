from flask import Flask
from flask import request

app = Flask(__name__)


#   默认首页
@app.route("/")
def hello_world():
    print(request.headers)  # 获取请求头
    print(request.args)  # 获取请求参数
    print(request.args['name'])  # 拿到请求参数中的某个key的val
    print(request.args.getlist('age'))  # 拿到请求参数中的多个相同key的val

    print(request.form)

    return "Hello World!"


@app.route(rule="/page1", methods=["post"])
def page():
    print(request.form)  # 获取表单原始数据
    print(request.form['name'])  # 拿到表单数据中的某个key的val
    print(request.form.getlist('age'))  # 拿到表单数据中的多个相同key的val

    return "Hello World!"


@app.route(rule="/page2", methods=["post"])
def page2():
    print(request.files)  # 获取表单原始数据
    print(request.files['avtar'])  # 拿到单个文件key的val对象
    print(request.files.getlist('avtar'))  # 拿到多个相同文件key的val对象

    print(request.files['avtar'].headers)  # Content-Disposition: form-data; name="avtar"; filename="hahaha.jpeg" Content-Type: image/jpeg
    print(request.files['avtar'].name)  # 获取请求参数名
    print(request.files['avtar'].stream)  # 获取文件流信息 <tempfile.SpooledTemporaryFile object at 0x000001EEE8DB59A0>
    print(request.files['avtar'].filename)  # 获取文件名.后缀名
    request.files['avtar'].save('./hahaha.jpeg')  # 保存文件到指定目录下

    return "Hello World!"


@app.route(rule="/page3", methods=["post"])
def page3():
    print(request.is_json)  # 判断请求是否是json请求
    print(request.json)  # 获取json原始数据
    print(request.json['name'])  # 拿到json的key的value

    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
