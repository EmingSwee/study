from sqlalchemy import create_engine  # 驱动引擎
from sqlalchemy.ext.declarative import declarative_base  # 数据库基类
from sqlalchemy.orm import sessionmaker  # 连接会话

# 也可以像下述一样一次性导入所有包就可以省略导入上面的三个包
from sqlalchemy import *
from sqlalchemy.orm import *


engine = create_engine(
    url="mysql+pymysql://root:123456@127.0.0.1:3306/test6?charset=utf8mb4",  # 如果继承驱动使用pymysql
    # url="mysql://root:123456@127.0.0.1:3306/test6?charset=utf8mb4", # 如果基层驱动使用MysqlDB
    echo=True,  # 当设置为True时会将orm语句转化为sql语句打印，一般在debug时使用
    pool_size=8,  # 连接池大小，默认5，0为无限制
    pool_recycle=60 * 30  # 设置数据库多久没连接就自动断开
)

# 设置数据库连接
DbSession = sessionmaker(bind=engine)
session = DbSession()

# 创建数据基类
Model = declarative_base()
