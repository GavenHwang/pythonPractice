# -*- coding:utf-8 -*-
import curlify
import requests

res = requests.request(url="https://www.baidu.com", method="get")
curl_str = curlify.to_curl(res.request)
print(curl_str)
