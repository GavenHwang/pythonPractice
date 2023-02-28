# -*- coding:utf-8 -*-
import threading
from time import sleep


def function(i):
    print("%s function called by thread %s \n" % (threading.currentThread().getName(), i))
    sleep(60)


threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()