# -*- coding:utf-8 -*-
import requests
import threading
from datetime import datetime


class cmdb_search():
    """资产并发查询"""
    def __init__(self):
        self.host = "http://10.10.21.7:6080"
        url_path = self.host + '/login/loginAuth.action'
        params = {
            'strUserName': 'cmdb',
            'strPassword': 'Gridview@123',
        }
        res = requests.post(url_path, data=params)
        self.cookie = res.cookies.get_dict()
        self.start_time = datetime.now()
        self.count = 0
        self.target_num = 2 ** 32
    def resource_linux_add_and_delete(self):
        # 查到就删除
        res = requests.request(method='GET',
                               url=self.host + '/resourcemanagement/api/resources/actions/query', cookies=self.cookie,
                               headers={'Accept': 'application/json, text/plain, */*',
                                        'Accept-Encoding': 'gzip, deflate',
                                        'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                        'Host': '10.10.21.7:6080', 'Referer': 'http://10.10.21.7:6080/web/index.html',
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                               params={'categoryId': '', 'resName': '', 'managerIp': '', 'bmcIp': '', 'type': 'simple',
                                       'start': '0', 'limit': '25', 'order': '', 'sort': ''},
                               data=None,
                               json=None,
                               )
        res_data = res.json().get("data", {}).get("data", [])
        resource_id = None
        for d in res_data:
            if d.get("manageHostName") == "node1007" and d.get("manageIp") == "10.10.21.7":
                resource_id = d.get("resourceId")
        requests.request(method='GET',
                         url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount', cookies=self.cookie,
                         headers={'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate',
                                  'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                  'Host': '10.10.21.7:6080', 'Referer': 'http://10.10.21.7:6080/web/index.html',
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                         params={'categoryId': '10026', 'resId': '10001'},
                         data=None,
                         json=None,
                         )

        requests.request(method='GET',
                         url=self.host + '/resourcemanagement/api/categories/all', cookies=self.cookie,
                         headers={'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate',
                                  'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                  'Host': '10.10.21.7:6080', 'Referer': 'http://10.10.21.7:6080/web/index.html',
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                         params=None,
                         data=None,
                         json=None,
                         )
        if resource_id:
            res = requests.request(method='DELETE',
                                   url=self.host + '/resourcemanagement/api/resources/batch',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                            'Host': '10.10.21.7:6080', 'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json={"delResIdList": [resource_id]},
                                   )
            if res.status_code == 200 and res.json().get("code") == "0":
                return 2
        else:
            # 查不到就创建
            res = requests.request(method='POST',
                                   url=self.host + '/resourcemanagement/api/resources/single',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive',
                                            'Host': '10.10.21.7:6080', 'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json={'categoryId': '10002', 'subCategoryId': '10002', 'modelId': '10002',
                                         'clusterId': 1001,
                                         'resourceName': 'node1007',
                                         'paramInfoList': [{'tempId': '10005', 'paramValue': '10.10.21.7'},
                                                           {'tempId': '10006', 'paramValue': '1'},
                                                           {'tempId': '10007', 'paramValue': ''},
                                                           {'tempId': '10008', 'paramValue': 'A410r-G'},
                                                           {'tempId': '10281', 'paramValue': 'node1007'},
                                                           {'tempId': '10285', 'paramValue': ''},
                                                           {'tempId': '10286', 'paramValue': ''},
                                                           {'tempId': '10287', 'paramValue': ''},
                                                           {'tempId': '10490', 'paramValue': ''},
                                                           {'tempId': '10493', 'paramValue': ''},
                                                           {'tempId': '10494', 'paramValue': ''},
                                                           {'tempId': '10495', 'paramValue': 'public'},
                                                           {'tempId': '10496', 'paramValue': '161'},
                                                           {'tempId': '10497', 'paramValue': 'v2c'},
                                                           {'tempId': '10499', 'paramValue': 'Sugon'},
                                                           {'tempId': '10508', 'paramValue': 'rack'},
                                                           {'tempId': '10509', 'paramValue': ''}],
                                         'dependantInfoList': []},
                                   )
            if res.status_code == 200 and res.json().get("code") == "0":
                return 1

    def cmdb_search(self):
        try:
            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '', 'resName': '', 'managerIp': '', 'bmcIp': '',
                                           'type': 'simple', 'start': '0', 'limit': '25', 'order': '', 'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10002', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10008', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10005', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10009', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10013', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10010', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10001', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/resources/actions/query',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10006', 'modelId': '', 'resName': '', 'managerIp': '',
                                           'bmcIp': '', 'type': 'simple', 'start': '0', 'limit': '25', 'order': '',
                                           'sort': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/alarmmonitor/resouce/alarmcount',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'categoryId': '10026', 'resId': '10001'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/categories/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/groups/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'start': '0', 'limit': '25', 'order': '', 'sort': 'ASC', 'search': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/clusters/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/groups/categories/details',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/groups/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'start': '0', 'limit': '25', 'order': '', 'sort': 'ASC', 'search': ''},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/clusters/all',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/resourcemanagement/api/groups/categories/details',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/queryAllMissionInfo.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/getProtocolInfo.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/ipmiView/queryInfoById.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data={'serialNumber': '', 'ipmiIP': '', 'groupName': '', 'limit': '25',
                                         'status': '0,1', 'start': '0', 'orderBy': 'discoverTime', 'sort': 'DESC',
                                         'missionId': '0'},
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/servicesmanage/services',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'nodeRole': '', 'orderBy': '', 'searchParam': '', 'sort': '', 'start': '0',
                                           'limit': '25'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/servicesmanage/noderole',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/servicesmanage/services',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params={'nodeRole': '', 'orderBy': '', 'searchParam': '', 'sort': '', 'start': '0',
                                           'limit': '25'},
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='GET',
                                   url=self.host + '/clustermonitor/api/servicesmanage/noderole',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/ipmiView/queryInfoById.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data={'serialNumber': '', 'ipmiIP': '', 'groupName': '', 'limit': '25',
                                         'status': '0,1', 'start': '0', 'orderBy': 'discoverTime', 'sort': 'DESC',
                                         'missionId': '0'},
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/ipmiView/queryInfoById.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data={'serialNumber': '', 'ipmiIP': '', 'groupName': '', 'limit': '25',
                                         'status': '0', 'start': '0', 'orderBy': 'discoverTime', 'sort': 'DESC',
                                         'missionId': '0'},
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/queryIntervalMissionInfos.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data=None,
                                   json=None,
                                   )
            self.count += 1

            res = requests.request(method='POST',
                                   url=self.host + '/discoverresource/ipmiView/queryInfoById.action',
                                   cookies=self.cookie,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive', 'Host': '10.10.21.7:6080',
                                            'Origin': 'http://10.10.21.7:6080',
                                            'Referer': 'http://10.10.21.7:6080/web/index.html',
                                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'},
                                   params=None,
                                   data={'serialNumber': '', 'ipmiIP': '', 'groupName': '', 'limit': '25',
                                         'status': '1', 'start': '0', 'orderBy': 'discoverTime', 'sort': 'DESC',
                                         'missionId': '0'},
                                   json=None,
                                   )
            self.count += 1
        except Exception as e:
            print(e.__str__())

    def loop_myself(self):
        while self.count < self.target_num:
            cmdb_search_obj.cmdb_search()
            print("=====%s接口调用%s次,预计还需%s=====" % (
            threading.currentThread().getName(), cmdb_search_obj.count, self.get_need_time()))

    def get_need_time(self):
        total_need_seconds = int(
            (float((datetime.now() - self.start_time).seconds)) / self.count * (self.target_num - self.count)
        )
        need_day = total_need_seconds // 3600 * 24
        need_hours = total_need_seconds // 3600 % 24
        need_minute = total_need_seconds // 60 % 60
        return "%s天%s小时%s分钟" % (need_day, need_hours, need_minute)

cmdb_search_obj = cmdb_search()
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        cmdb_search_obj.loop_myself()


if __name__ == "__main__":
    bingfashu = 100
    threads = []
    for i in range(bingfashu):
        threads.append(myThread(i, "Thread-%s" % i, i))
    for j in range(len(threads)):
        threads[j].start()
    for k in range(len(threads)):
        threads[k].join()
