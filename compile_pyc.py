# -*- coding:utf-8 -*-
import os.path
import py_compile
import sys

f = sys.argv[-1]
path = os.path.join(os.path.dirname(__file__), f)
py_compile.compile(path, cfile=path + "c")
