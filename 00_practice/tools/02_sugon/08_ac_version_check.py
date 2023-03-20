# -*- coding:utf-8 -*-
import requests


def get_version(host, path):
    res = requests.get(host + path)
    if res.status_code == 200:
        return res.text
    else:
        return host+path+"地址不正确，或者不存在！\n"


def print_version(version_path_dir):
    for k, v in version_path_dir.items():
        print(get_version(host, v), end="")


if __name__ == "__main__":
    host = "https://itos2.sugon.com"
    version_path_dir = {
        "sacp": "/ac/version.html",
        "ac-ui": "/ac/console3/version.html",
        "easyop": "/itos/version.html",
        "sso": "/sso/version.html",
        "acx-appcenter": "/acx/appcenter/version.html",
        "acx-jobgather": "/acx/jobgather/version.html",
        "acx-jobmgt": "/acx/jobmgt/version.html",
        "acx-resource": "/acx/resource/version.html",
        "acx-user": "/acx/user/version.html",
        "acx-authority": "/acx/authority/version.html",
        "acx-gateway": "/acx/gateway/version.html",
        "message": "/message/version.html",
    }
    print_version(version_path_dir)
