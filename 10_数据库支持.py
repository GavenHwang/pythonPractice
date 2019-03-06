# -*- conding: utf-8 -*-

# apilevel       Python DB API版本 1.0,2.0
# threadsafety  模块的线程安全等级 0~3
# paramstyle    参数风格 format、pyformat、qmark、numeric、named

# dns：数据源名称（非必输）、user、password、host、database
# close()、commit()、rollback()、cursor()

# 游标方法:
# callproc(name[,params])   :使用给定的名称和参数调用已命名的数据库过程
# close()                   :关闭游标
# execute(oper[,params])    :指哪个行一个SQL操作,可能带有参数
# executemany(oper, pseq)   :对序列中的每个参数执行SQL操作
# fetchone()                :把查询结果集中的下一行保存为序列,或者None
# fetchmany([size])         :获取查询结果集中的多行默认尺寸为arraysize
# fetchall()                :将所有(剩余)的行作为序列的序列
# nextset()                 :跳至下一个可用的结果集
# setinputsizes(sizes)      :为参数预先定义内存区域
# setoutputsize(size[,col]) :获取的大数据值设定缓存尺寸

# import sqlite3
#
# conn = sqlite3.connect("database.db")
# curs = conn.cursor()
# conn.commit()
# conn.close()

# 创建和填充表
# import fileinput
# import re
# import sqlite3
# from pip._vendor import chardet
#
#
# def convert(value):
#     if value.startswith('~'):
#         return value.strip('~')
#     return float(value) if value else ''
#
# conn = sqlite3.connect('food_des.db')
# curs = conn.cursor()
#
# curs.execute('''
#     CREATE TABLE food_des(
#         NDB_No	TEXT,
#         FdGrp_Cd	TEXT,
#         Long_Desc	TEXT,
#         Shrt_Desc	TEXT,
#         Com_Name	TEXT,
#         ManufacName	TEXT,
#         Survey	TEXT,
#         Ref_Desc	TEXT,
#         Refuse  FLOAT,
#         Sci_Name	TEXT,
#         N_FActor	FLOAT,
#         Pro_Factor_	FLOAT,
#         Fat_Factor_	FLOAT,
#         CHO_Factor	FLOAT)
# ''')
#
# query = 'INSERT INTO food_des VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
#
# for line in fileinput.input(r'FOOD_DES.txt', mode='rb'):
#     encoding = chardet.detect(line).get('encoding')
#     line = line.decode(encoding)
#     r = r'(.*)\r\n$'
#     fields = re.compile(r).match(line).group(1).split('^')
#     vals = [convert(f) for f in fields]
#     if vals:
#         curs.execute(query, vals)
# conn.commit()
# conn.close()

# 搜索和处理结果
import sqlite3, sys

conn = sqlite3.connect('food_des.db')
curs = conn.cursor()

query = "select * from food_des where NDB_NO = '%s'" % '01002'
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('%s: %s' % pair)
