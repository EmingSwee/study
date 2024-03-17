from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test6?charset=utf8'
    db = SQLAlchemy(app)


    class User(db.Model):
        __tablename__ = 'user'  # 要操作的表名
        id = db.Column(db.Integer, primary_key=True)  # 表字段
        userName = db.Column(db.String(255))

        def __repr__(self):
            return f"<{self.userName} {self.__class__.__name__}>"


    db.create_all()  # 数据迁移命令，没有这个就没办法建立新表


@app.route('/')
def index():
    users = User.query.filter(User.userName != '2').all()
    print(users.userName)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
