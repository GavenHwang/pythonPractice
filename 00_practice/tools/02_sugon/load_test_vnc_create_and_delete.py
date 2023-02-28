# -*- coding:utf-8 -*-
import requests


class vnc_create_and_delete():
    host = "http://10.10.21.7:6080"
    cookie = None

    def on_start(self):
        pass

    def __init__(self):
        url_path = self.host + '/login/loginAuth.action'
        params = {
            'strUserName': 'hll_0208',
            'strPassword': 'hll_0208hll_0208',
        }
        res = requests.post(url_path, data=params)
        self.cookie = res.cookies.get_dict()
        self.index = 1

    def on_stop(self):
        pass

    def vnc_create_and_delete(self):
        """查询到vnc会话就截图并删除，查询不到就直接创建"""
        try:
            res1 = requests.request(method='POST',
                                    url=self.host + '/desktopandapp/api/desktopApp/list',
                                    cookies=self.cookie,
                                    headers={'Accept': 'application/json, text/plain, */*',
                                             'Accept-Encoding': 'gzip, deflate',
                                             'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                             'Host': '10.10.21.7:6080',
                                             'Origin': 'http://10.10.21.7:6080',
                                             'Referer': 'http://10.10.21.7:6080/web/index.html',
                                             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                    params=None,
                                    data=None,
                                    json={'limit': 217778356, 'sort': 'DESC', 'start': 0, 'orderBy': 'jobs'},
                                    )
            if res1.status_code == 200 and res1.json().get("data", {}).get("list"):
                res_data = res1.json().get("data", {}).get("list")[0]
                res2 = requests.request(method='GET',
                                        url=self.host + '/desktopandapp/api/vncs/pngs/' + res_data.get("name"),
                                        cookies=self.cookie,
                                        headers={'Accept': 'application/json, text/plain, */*',
                                                 'Accept-Encoding': 'gzip, deflate',
                                                 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                                 'Host': '10.10.21.7:6080',
                                                 'Referer': 'http://10.10.21.7:6080/web/index.html',
                                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                        params={
                                            'sid': res_data.get("sid"),
                                            'sName': res_data.get("name"),
                                            'password': res_data.get("passwd"),
                                            'ip': res_data.get("ip"),
                                            'r': '0.2666799708897529'
                                        },
                                        data=None,
                                        json=None,
                                        )
                if res2.status_code == 200 and res2.json().get("code") == "0":
                    print("=======vnc会话截图成功！======")
                sessionId = res_data.get("sessionId")
                requests.request(method='DELETE',
                                 url=self.host + '/desktopandapp/api/desktopApp/deletes',
                                 cookies=self.cookie,
                                 headers={'Accept': 'application/json, text/plain, */*',
                                          'Accept-Encoding': 'gzip, deflate',
                                          'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                          'Host': '10.10.21.7:6080',
                                          'Origin': 'http://10.10.21.7:6080',
                                          'Referer': 'http://10.10.21.7:6080/web/index.html',
                                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                 params={'sessionIds': sessionId},
                                 data=None,
                                 json=None,
                                 )
                print("=======删除vnc会话：%s======" % str(res_data))
            else:
                res = requests.request(method='POST',
                                       url=self.host + '/desktopandapp/api/vncs/vncsession',
                                       cookies=self.cookie,
                                       headers={'Accept': 'application/json, text/plain, */*',
                                                'Accept-Encoding': 'gzip, deflate',
                                                'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                                'Host': '10.10.21.7:6080',
                                                'Origin': 'http://10.10.21.7:6080',
                                                'Referer': 'http://10.10.21.7:6080/web/index.html',
                                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                       params=None,
                                       data=None,
                                       json={},
                                       )
                print("=======创建第%s个vnc会话：%s======" % (self.index, str(res.json().get("data"))))
                self.index = self.index + 1
        except Exception as e:
            print(e.__str__())


vnc = vnc_create_and_delete()
while True:
    vnc.vnc_create_and_delete()
