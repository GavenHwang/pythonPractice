# -*- coding: utf-8 -*-
import json
import os
import random
import re
import sys
import time
from concurrent.futures import thread
from pathlib import Path
import requests
import yaml
from assertpy import assert_that
# from filelock import FileLock
# from pykeyboard import PyKeyboard

# PathPractice = "/Users/gaven/fsdownload/i18n/zh"
# for file_name in os.listdir(PathPractice):
#     with open(PathPractice + "/" + file_name, "r") as file_read_obj:
#         file_str = file_read_obj.read()
#         read_str = file_str.replace("\:", ":").replace("\!", "!").replace("\ ", " ").replace("\=", "=").encode("utf8").\
#             decode("unicode_escape")
#     with open(PathPractice + "/" + file_name, "w") as file_write_obj:
#         file_write_obj.write(read_str)

# res = requests.post("http://10.0.35.17/api/queryRAPModel.do?projectId=15")
# res_json = res.json()
print(time.time())
print(time.time() + 1000)
print(time.time())
time.sleep(2)
print(time.time())