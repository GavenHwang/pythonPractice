# -*- coding:utf-8 -*-
import os
from pathlib import Path


print(os.path.realpath(__file__))
print(os.path.abspath(__file__))

# 当前目录
os_cwd = os.getcwd()
print(os_cwd)
pathlib_cwd = Path.cwd()
print(pathlib_cwd)

# 上一级目录
os_parent_path = os.path.dirname(os_cwd)
print(os_parent_path)
pathlib_parent_path = pathlib_cwd.parent
print(pathlib_parent_path)

# 拼接目录
os_join_path = os.path.join(os_parent_path, "hello")
print(os_join_path)
pathlib_join_path = pathlib_parent_path.joinpath("hello")
print(pathlib_join_path)

# 创建文件夹并重命名
# os.makedirs(os.path.join('project', 'test'), exist_ok=True)
# Path('project/test').mkdir(parents=True, exist_ok=True)
# 将test.txt 重命名为 project/tests.txt
# os.rename('test.txt', os.PathPractice.join('project', 'tests.txt'))
# Path('test.txt').rename('project/test.txt')