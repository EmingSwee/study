import time
from threading import Thread
from multiprocessing import Process

#   子线程要执行的代码
def thread_func(name):
    print(f'{name}开始执行')

#   子进程内创建多路子线程
def worker(name):
    time.sleep(2)
    print(f'{name}创建了子线程')
    for i in range(5):
        t = Thread(target=thread_func, args=(name,))
        t.start()


if __name__ == '__main__':
    t1 = Process(target=worker, args=("haha",))
    t1.start()
    print("主进程结束")
