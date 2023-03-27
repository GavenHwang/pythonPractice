#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import argparse
from multiprocessing import Process
# from multiprocessing import cpu_count


def exec_func(et):
    end_time = time.time() + et
    while time.time() < end_time:
        for i in range(0, 9600000):
            pass
        time.sleep(0.01)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='runing')
    parse.add_argument("-c", "--count", default=1, help='cpu count')
    parse.add_argument("-m", "--memory", default="1M", help='memory')
    parse.add_argument("-t", "--time", default=10, help='cpu time')
    args = parse.parse_args()
    cpu_logical_count = int(args.count)
    memory_used = 1
    if "M" in args.memory or "m" in args.memory:
        memory_used = int(str(args.memory).strip().replace("M", ""))
    elif "G" in args.memory or "g" in args.memory:
        memory_used = int(str(args.memory).strip().replace("G", "")) * 1024
    else:
        parse.error("-m %s 单位错误，请使用G或者M" % args.memory)

    eat_time = int(args.time)

    _doc = """
    python runing.py -c 2 -m 1G -t 30
    -c 指定cpu核数，默认为1
    -m 内存占用，单位M、G，默认为1M
    -t 占用时间，单位秒，默认为10
    """

    print("\n====================使用说明=========================")
    print("{0}".format(_doc))
    print("====================================================")
    print('当前占用CPU核数:{0}'.format(cpu_logical_count))
    print('内存预计占用:{0}'.format(args.memory))
    print('预计占用{0}秒'.format(eat_time))
    print('资源占用中......')

    m_list = []
    try:
        # 内存占用
        for i in range(memory_used):
            m_list.append(' ' * (1 * 1024 * 1024))
    except MemoryError:
        print("剩余内存不足，内存有溢出......")

    ps_list = []
    try:
        for i in range(0, cpu_logical_count):
            ps_list.append(Process(target=exec_func, args=(eat_time,)))

        for p in ps_list:
            p.start()

        for p in ps_list:
            p.join()

        m_list.clear()
        print("资源占用结束!")
    except KeyboardInterrupt:
        m_list.clear()
        print("资源占用结束!")
