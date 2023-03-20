# -*- coding:utf-8 -*-
import argparse
import re
from time import sleep
import requests
import xlrd2 as xlrd


def get_args():
    """处理请求参数"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-JSESSIONID', type=str, dest='JSESSIONID', help='JSESSIONID', default="############")
    parser.add_argument('-excel_name', type=str, dest='excel_name', help='带路径的excel文件名', default=r"C:\Users\Gaven\Downloads\参与人员.xlsx")
    args = parser.parse_args()
    if not args.JSESSIONID or not args.excel_name:
        print(parser.print_help())
    return args


def read_excels(file_name):
    """读取excel文件"""
    unitId_dir = {
        "（北京）有限公司": "#######",
        "大学": "##########",
        "设计有限公司": "##########",
    }
    education_dir = {
        "研究生": "01",
        "本科": "02",
        "专科": "03",
        "其他": "04",
    }
    degree_dir = {
        "博士": "01",
        "硕士": "02",
        "学士": "03",
        "其他": "04",
    }
    title_dir = {
        "正高级": "A",
        "副高级": "B",
        "中级": "C",
        "初级": "D",
        "其他": "E",
    }
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    datas = []
    for rx in range(1, sheet.nrows):
        try:
            row = sheet.row(rx)
            line = {
                "submitToken": "",
                "id": "",
                "ssXmjdId": "",
                "ssKtjdId": "",
                "name": row[0].value,  # 姓名
                "unitId": unitId_dir.get(row[1].value),  # 所在单位
                "unitAcademy": row[2].value,  # 所在院系
                "sn": str(row[3].value),  # 序号
                "sex": "01" if row[4].value == '男' else "02",  # 性别
                "education": education_dir.get(row[5].value),  # 学历
                "degree": degree_dir.get(row[6].value),  # 最高学位
                "title": title_dir.get(row[7].value),  # 专业技术职称
                "sfgzxsr": "1" if row[8].value == '是' else '0',  # 是否有工资收入
                "type": "C" if row[9].value == '项目/课题骨干' else 'D',  # 在项目中的角色
                # "isKt": "",
                "isKtYoung": "",
                "continent": "10",  # 大洲 亚洲
                "country": "1001",  # 国家或地区 中华人名共和国
                "cardType": "1",  # 证件类型 身份证
                "cardNumber": row[13].value,  # 证件号码
                "birthday": row[14].value,  # 出生日期
                "isStudent": "1" if row[15].value == '是' else '0',  # 是否在校学生
                "duty": row[16].value,  # 职务
                "major": row[17].value,  # 专业
                "phone": row[18].value,  # 固定电话
                "mobile": row[19].value,  # 移动电话
                "email": row[20].value,  # 电子邮箱
                "manMonth": row[21].value,  # 投入本项目的全时工作时间（人月）
                "tasksKt": row[22].value,  # 在课题中分担的任务
                # "postcode": row[23].value,  # 邮政编码
                # "address": row[24].value,  # 通信地址
            }
            datas.append(line)
        except:
            print(sheet.row(rx))
            raise ValueError("第%s数据有误！" % str(rx + 1))
    return datas


def get_submit_token(cookies, ssXmjdId, jdId):
    """获取提交表单token"""
    res = requests.post(
        "https://service2.most.gov.cn/KG145-YF-SBS-DX-V202106/f/subject/person/form?ssXmjdId=%s&ssKtjdId=%s" % (ssXmjdId, jdId),
        cookies=cookies)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("获取token失败！")
    line = res.text
    searchObj = re.search(r'name="submitToken" value="(.*?)"', line, re.M | re.I)
    if not searchObj:
        print(line)
        raise ValueError("获取token失败！")
    submitToken = searchObj.group(1)
    return submitToken


def save(data, submit_token, cookies):
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    res = requests.post(url="https://service2.most.gov.cn/KG145-YF-SBS-DX-V202106/f/subject/person/save",
                        headers=headers, cookies=cookies, data=data)
    if res.status_code != 200:
        print(data)
        print(res.text)
        raise ValueError("保存表单失败！")
    print(data['name'], ' ----- ', res.text)


if __name__ == "__main__":
    args = get_args()
    args.JSESSIONID = '64F2670494B0CF62740725AD2F4C2B2E'
    datas = read_excels(args.excel_name)
    cookies = {
        "JSESSIONID": args.JSESSIONID,
        "uid": "7580bef3cd4282eb545ce6a92f1f5b5c",
    }
    ssXmjdId = "**********"
    ssKtjdId = "**********"
    for data in datas:
        # jdId = get_jd_id(cookies)
        submit_token = get_submit_token(cookies, ssXmjdId, ssKtjdId)
        data["submitToken"] = submit_token
        data["ssXmjdId"] = ssXmjdId
        data["ssKtjdId"] = ssKtjdId
        save(data, submit_token, cookies)
