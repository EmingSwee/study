import model  # 导入model包中的创建好的model类对象


# 创建一个对象类用来映射数据库表的对象
class User(model.Model):
    __tablename__ = 'user'  # 要操作的表名
    id = model.Column(model.Integer, primary_key=True)  # 表字段
    userName = model.Column(model.String(255))

    # 加上这个私有方法后可以在进行select * from db的时候显示出具体字段的值，而不是对象内存信息
    def __repr__(self):
        return f"<{self.userName} {self.__class__.__name__}>"


if __name__ == '__main__':
    model.Model.metadata.create_all(model.engine)  # 创建连接信息

    data = model.session.query(User).all()  # 进行查询操作select * from db

    # 遍历查询字段
    for d in data:
        print(d.userName, d.id)

    # 获取一条主键id为2的数据
    s = model.session.get(User, 1)
    print(s, s.userName, s.id)

    # 利用filter过滤查询
    data_list = model.session.query(User).filter(User.id == 1).all()
    for d in data_list:
        print(d.userName, d.id)

    # 添加数据
    dd = User(
        userName='lueluelue',
    )

    model.session.add(dd)
    model.session.commit()

    # 添加多条数据
    dd_list = [
        User(userName='lueluelue', ),
        User(userName='啦啦啦', )
    ]
    model.session.add_all(dd_list)
    model.session.commit()

    # 修改操作
    mm = model.session.query(User).filter_by(userName="哈哈哈").first()
    if mm:
        mm.userName = '嘻嘻嘻'
        model.session.commit()
    else:
        print("err")

    # 修改多条
    model.session.query(User).filter(User.id < 5).update({'userName': '哼'})
    model.session.commit()

    # 删除操作
    dele = model.session.query(User).filter_by(userName="lueluelue").first()
    if dele:
        dele.delete()
        model.session.commit()

    # 批量删除
    model.session.query(User).filter(User.id > 3).delete()
    model.session.commit()
