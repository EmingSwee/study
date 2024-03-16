import random
import threading


"""模拟发送邮件函数"""


def sendEmail(i):
    random.random()
    print(f'发送了第{i}个邮件')


if __name__ == '__main__':
    pList = []  # 存放子线程对象列表

    for i in range(10):  # 模拟要发送的邮件数量

        p = threading.Thread(target=sendEmail, args=(i,))  # 创建子线程

        p.start()  # 运行子线程

        pList.append(p)  # 把创建好的子线程对象装入列表

    for p in pList:  # 从列表读取子线程对象完成阻塞操作
        p.join()

    print('邮件发送完成')

# 创建子进程实现并发发送邮件
