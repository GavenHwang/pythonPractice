# -*- coding:utf-8 -*-
import atexit
import os


@atexit.register
def remove_lock_file():
    if os.path.exists('file.lock'):
        os.remove('file.lock')


def create_lock_file():
    if not os.path.exists('file.lock'):
        with open('file.lock', 'w') as f:
            pass
        return True
    else:
        return False


from multiprocessing import Process


def open_file():
    if create_lock_file():
        print('hello')


Process(target=open_file).start()
Process(target=open_file).start()
