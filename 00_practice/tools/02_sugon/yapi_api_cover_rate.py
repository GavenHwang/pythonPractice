# -*- coding:utf-8 -*-
import re

import requests
import xlsxwriter


def login_yapi(username, password):
    res = requests.request(method="post", url="http://10.0.41.74:3000/api/user/login_by_ldap",
                           json={"email": username, "password": password})
    cookie = res.cookies.get_dict()
    return cookie


def get_yapi_apis_json(username, password, pid):
    cookie = login_yapi(username, password)
    res = requests.request(method="get",
                           url="http://10.0.41.74:3000/api/plugin/export?type=json&pid=%s&status=all&isWiki=false" % pid,
                           cookies=cookie)
    return res.json()


def get_is_cover(path, jmeter_apis_txt, python_apis_txt):
    is_cover = "否"
    jmeter = None
    python = None
    if str(path).startswith("/"):
        path = path[1:]
    pattern = None
    if "{" in path and "}" in path:
        pattern = r'%s' % re.sub(r'\{.*\}', "(.+)", path)
    if path in jmeter_apis_txt or (pattern and re.search(pattern, jmeter_apis_txt, re.M)):
        is_cover = "是"
        jmeter = "jmeter"
    if path in python_apis_txt or (pattern and re.search(pattern, python_apis_txt)):
        is_cover = "是"
        python = "python"
    return is_cover, jmeter, python


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as fr:
        txt = fr.read()
    return txt


def get_txt_style(workbook):
    # 标题
    title_style = workbook.add_format({
        'font_name': "Calibri",  # 字体
        'font_size': 16,  # 字体大小
        'font_color': "#000000",  # 字体颜色
        'bold': True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'center',  # 左右对齐方式
        'valign': 'vcenter',  # 上下对齐方式
        'fg_color': '#ffffff',  # 背景色
        'num_format': 0,  # 数字、日期格式化  '￥#,##0.00'、'yyyy-m-d h:mm:ss'
    })
    title_style.set_text_wrap()
    # 小标题
    sub_title_style = workbook.add_format({
        'font_name': "Calibri",  # 字体
        'font_size': 14,  # 字体大小
        'font_color': "#000000",  # 字体颜色
        'bold': True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'center',  # 左右对齐方式
        'valign': 'vcenter',  # 上下对齐方式
        'fg_color': '#538dd5',  # 背景色
        'num_format': 0,  # 数字、日期格式化  '￥#,##0.00'、'yyyy-m-d h:mm:ss'
    })
    sub_title_style.set_text_wrap()
    # 正文
    text_style = workbook.add_format({
        'font_name': "Calibri",  # 字体
        'font_size': 10,  # 字体大小
        'font_color': "#000000",  # 字体颜色
        'bold': False,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'left',  # 左右对齐方式
        'valign': 'vcenter',  # 上下对齐方式
        'fg_color': '#ffffff',  # 背景色
        'num_format': 0,  # 数字、日期格式化  '￥#,##0.00'、'yyyy-m-d h:mm:ss'
    })
    text_style.set_text_wrap()
    # 正文绿色背景
    # 正文
    text_green_background_style = workbook.add_format({
        'font_name': "Calibri",  # 字体
        'font_size': 10,  # 字体大小
        'font_color': "#000000",  # 字体颜色
        'bold': False,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'left',  # 左右对齐方式
        'valign': 'vcenter',  # 上下对齐方式
        'fg_color': '#00b050',  # 背景色-绿色
        'num_format': 0,  # 数字、日期格式化  '￥#,##0.00'、'yyyy-m-d h:mm:ss'
    })
    text_green_background_style.set_text_wrap()
    return title_style, sub_title_style, text_style, text_green_background_style


def write_api_cover_excel(username, password, pid, excel_name, jmeter_apis_txt, python_apis_txt):
    # with open('ai2.8.json', 'r') as fr:
    #     json_file = fr.read()
    # yapi_api_jsons = json.loads(json_file)
    if not str(excel_name).endswith(".xlsx"):
        excel_name += ".xlsx"
    yapi_api_jsons = get_yapi_apis_json(username, password, pid)
    workbook = xlsxwriter.Workbook(excel_name)
    worksheet = workbook.add_worksheet()
    title_style, sub_title_style, text_style, text_green_background_style = get_txt_style(workbook)
    sub_titles = ["模块", "接口地址", "接口名称", "是否覆盖", "jmeter", "python"]
    for t in range(len(sub_titles)):
        worksheet.write(0, t, sub_titles[t], sub_title_style)
    row = 1
    for i in yapi_api_jsons:
        if type(i.get("list")) == list and len(i.get("list")) > 1:
            worksheet.merge_range(row, 0, row + len(i.get("list")) - 1, 0, i.get("name"), text_style)
        else:
            worksheet.write(row, 0, i.get("name"))
        for j in i.get("list", []):
            is_cover, jmeter, python = get_is_cover(j.get("path"), jmeter_apis_txt, python_apis_txt)
            txt_style = text_green_background_style if is_cover == "是" else text_style
            worksheet.write(row, 1, j.get("path"), txt_style)
            worksheet.write(row, 2, j.get("title"), txt_style)
            worksheet.write(row, 3, is_cover, txt_style)
            worksheet.write(row, 4, jmeter, txt_style)
            worksheet.write(row, 5, python, txt_style)
            row += 1
    col_width = [36, 72, 36, 24, 12, 12]
    for i in range(len(col_width)):
        worksheet.set_column(i, i, col_width[i])
    workbook.close()


if __name__ == '__main__':
    # 统计方法：
    # 1. 从35.29上导出python、jmeter接口用例，保存为文本文件
    # cat /root/.jenkins/workspace/test_gv_suites/e2e/logs/e2e_test_2023-02-18.log | grep 'he response of' | awk -F ' ' '{print $11}' | uniq > /root/python_apis.txt
    # grep -r -n -E '<stringProp name="HTTPSampler.path">.+</stringProp>' /root/.jenkins/workspace/Gridview_trunk_api_test_Slurm/testcase/ | awk -F '>|<' '{print $3}' | uniq > /root/jmeter_apis.txt
    # grep -r -n -E '<stringProp name="HTTPSampler.path">.+</stringProp>' /root/.jenkins/workspace/AI-trunk-api-test-slurm/testcase | awk -F '>|<' '{print $3}' | uniq > /root/jmeter_ai_apis.txt
    # 2. 从yapi上导出gv5.7项目的json格式接口文档
    # 3. 遍历yapi接口列表，逐个判断是否包含在步骤1中导出的文件中
    ### GV5.7
    python_apis_txt = read_file("python_gv_apis.txt")
    jmeter_apis_txt = read_file("jmeter_gv_apis.txt")
    write_api_cover_excel(username="huangleilei", password="sugon;123", pid=284, excel_name="gv5.7接口覆盖列表",
                          jmeter_apis_txt=jmeter_apis_txt, python_apis_txt=python_apis_txt)
    ### AI2.8
    # jmeter_apis_txt = read_file("jmeter_ai_apis.txt")
    # write_api_cover_excel(username="huangleilei", password="sugon;123", pid=282, excel_name="ai2.8接口覆盖列表",
    #                       jmeter_apis_txt=jmeter_apis_txt, python_apis_txt="")
