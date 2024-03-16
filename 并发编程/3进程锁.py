import json
from multiprocessing import Lock, Process


def queryCount(name):
    with open("file.txt", "r") as f:
        data = json.load(f)
        print(f"{name}查询余票：{data['count']}")
        return data


def buyTicket(name):
    data = queryCount(name)
    if data['count'] > 0:
        data['count'] -= 1
        print(f'{name}购票成功')
    else:
        print(f'{name}购票失败')
    json.dump(data, open("file.txt", "w"))


def run(name, lock):
    with lock:
        buyTicket(name)


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=run, args=(f"用户{i}", lock))
        p.start()

# 利用进程锁实现并发安全完成并发购票
