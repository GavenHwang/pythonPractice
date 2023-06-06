# -*- coding:utf-8 -*-
import openpyxl

# 获取工作簿对象
wb = openpyxl.load_workbook('1.xlsx')

# 获取工作表对象,三种方法
sheet1 = wb.worksheets[0]
sheet2 = wb['成绩表']
sheet3 = wb[wb.sheetnames[2]]
print(sheet1, sheet2, sheet3)

# 写入多个单元格(追加模式，不会覆盖之前的，从有数据的下一行开始)
sheet1.append(['王五', '三年级二班', '10岁'])


# 保存
wb.save('1.xlsx')

