import multiprocessing as m
import random
from multiprocessing import current_process

"""模拟发送邮件函数"""


def sendEmail(i):
    p = current_process()
    print(f'当前进程名{p.name},当前进程id{p.pid}')
    random.random()
    print(f'发送了第{i}个邮件')


if __name__ == '__main__':
    pList = []  # 存放子线程对象列表

    for i in range(10):  # 模拟要发送的邮件数量

        p = m.Process(target=sendEmail, args=(i,))  # 创建子进程

        p.start()  # 运行子进程

        pList.append(p)  # 把创建好的子进程对象装入列表

    for p in pList:  # 从列表读取子进程对象完成阻塞操作
        p.join()

    print('邮件发送完成')

# 创建子进程实现并发发送邮件
