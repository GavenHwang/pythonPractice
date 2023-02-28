# -*- coding: utf-8 -*-
import os


PathPractice = "/Users/gaven/fsdownload/i18n/zh"
for file_name in os.listdir(PathPractice):
    with open(PathPractice + "/" + file_name, "r") as file_read_obj:
        file_str = file_read_obj.read()
        read_str = file_str.replace("\:", ":").replace("\!", "!").replace("\ ", " ").replace("\=", "=").encode("utf8").\
            decode("unicode_escape")
    with open(PathPractice + "/" + file_name, "w") as file_write_obj:
        file_write_obj.write(read_str)
