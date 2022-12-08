# -*- coding:utf-8 -*-
import json
import re
from bs4 import BeautifulSoup
import requests


def login1():
    url = 'https://itos.sugon.com/sso/login'
    res = requests.get(url)
    res_html = res.text
    execution_str = re.search(r"name=\"execution\" value=\"(.*?)\" />", res_html)[1]
    return execution_str


def login2(execution=""):
    url = 'https://itos.sugon.com/sso/login'
    params = {
        "username": "hll_ordinary",
        "password": "111111a",
        "_eventId": "submit",
        "submit": "登录",
        "execution": execution,
        "mode": "0",
    }
    res = requests.post(url, data=params)
    cookies = res.cookies
    return cookies


def login3():
    url = 'https://itos.sugon.com/ac/api/auth/loginSso.action'
    res = requests.post(url, cookies=login2(execution=login1()))
    print(repr(res.json()))


if __name__ == "__main__":
    login3()