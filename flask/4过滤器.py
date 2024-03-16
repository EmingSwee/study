from flask import Flask, render_template
from filter import FILTERS

app = Flask(__name__, template_folder="templates")

# 完成对自定义过滤器函数的注册
for k, v in FILTERS.items():
    app.add_template_filter(v, k)


@app.route("/")
def index():
    book_list = [
        {"id": 1, "price": 11.111, "title": "啦啦啦", "author": "<img src='/static/image/aa.jpg'>"},
        {"id": 2, "price": 12.112, "title": "嘟嘟嘟", "author": "<img src='/static/image/aa.jpg'>"},
        {"id": 3, "price": 13.113, "title": "嘻嘻嘻", "author": "<img src='/static/image/aa.jpg'>"}
    ]
    html = render_template("index.html", **locals())
    return html


# 自定义过滤器
@app.route("/xixi")
def index2():
    html = render_template("index2.html", **locals())
    return html


if __name__ == "__main__":
    app.run(debug=True)

# 本案例配合templates目录内index.html和static目录内图片完成对小数点的格式化和图片资源的展示
# 第二个路由配合filter文件和index2.html完成了自定义过滤器的小数点格式化操作
