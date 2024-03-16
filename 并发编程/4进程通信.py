from multiprocessing import Process, Queue


def pp(con, queue):
    res = eval(con)
    print(f'子进程的计算结果为：{res}')
    queue.put(res)  # 通过把计算结果放入queue中，实现主线程可以通过queue拿到子线程的数据完成进程间通信效果


if __name__ == '__main__':
    q = Queue()
    p = Process(target=pp, args=("1+2+3", q)).start()
    print(f'子进程返回给主进程的结果为：{q.get()}')
