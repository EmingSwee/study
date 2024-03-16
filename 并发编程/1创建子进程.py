import multiprocessing as m
import os


def pro():
    print("先开门")


def wash(name):
    print(f'{name}洗了手')


def eat(name):
    print(f'{name}吃了饭')


if __name__ == '__main__':
    print('父进程编号：', os.getpid())
    p1 = m.Process(target=pro)
    p2 = m.Process(target=wash, args=("小明",))
    p3 = m.Process(target=eat, args=("小明",))
    p1.start()
    p2.start()
    p3.start()

    print('主进程结束')

# 创建子进程
