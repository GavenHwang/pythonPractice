# -*- coding:utf-8 -*-
import threading
import time


class SingleTon(object):
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if cls.instance:
                return cls.instance
            time.sleep(0.1)
            cls.instance = object.__new__(cls)
            return cls.instance


def task():
    obj = SingleTon('Arno')
    print(obj)


for i in range(10):
    t = threading.Thread(target=task)
    t.start()