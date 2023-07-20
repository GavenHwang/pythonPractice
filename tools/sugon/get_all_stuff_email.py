# -*- coding:utf-8 -*-
with open("all_stuff_email.txt", 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
txt = ""
for line in lines:
    stuff = line.split("\t")
    txt += '"%s" <%s>, ' % (stuff[1], stuff[4])
print(txt)
