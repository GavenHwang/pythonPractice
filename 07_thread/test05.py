# -*- coding:utf-8 -*-
import threading
import urllib3 as urllib3
from requests import request

urllib3.disable_warnings()


def get_names(i):
    names = []
    for j in range(100):
        names.append("oapi_i%s_%s" % (i, j))
    return names


def function(i, names):
    for name in names[i]:
        res_json = request(
            method="post", url="https://itos.sugon.com/ac/openapi/v2/user/member",
            headers={
                'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wdXRlVXNlciI6Im9hcGlfY29tX2xlYWRlcjEiLCJhY2NvdW50U3RhdHVzIjoiTm9ybWFsIiwiY3JlYXRvciI6ImFjIiwicm9sZSI6IjEiLCJleHBpcmVUaW1lIjoiMTY4NTg0Nzc5MTIxMCIsImNsdXN0ZXJJZCI6IjExMzAzIiwiaW52b2tlciI6Ijg4OTVlYWEzNzcyMmRhNjEzMTlkZjkxMzhkMDcyYjI2IiwidXNlciI6Im9hcGlfY29tX2xlYWRlcjEiLCJ1c2VySWQiOiIxMTY3NzM3NTQ0MiJ9.WSNfdFEyzFLutpgac1hs5m3yQp_JphU_tU_35U4o548',
                'clusterIds': '11303',
                'userFullName': 'oapi_{}'.format(name),
                'userName': 'oapi_{}'.format(name),
                'email': 'oapi_{}@sugon.com'.format(name),
                'mobilephoneNum': '',
                'password': '111111a'
            },
            data=None,
            verify=False
        ).json()
        print(name, res_json)
        # assert res_json.get("code") == "1014"
        # assert res_json.get("msg") == "用户添加成功，邮件发送失败，请联系销售经理重置当前用户密码"


if __name__ == '__main__':
    names = []
    threads = []
    for i in range(50):
        names.append(get_names(i))
        t = threading.Thread(target=function, args=(i, names))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
