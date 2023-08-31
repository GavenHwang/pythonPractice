# -*- coding:utf-8 -*-
import json
import urllib3
from requests import request

urllib3.disable_warnings()

project_names = [
    'sacp4.x',
    'ac-ui',
    'easyop',
    'sso',
    'acx-bizanalysis',
    'acx-resource',
    'acx-fund',
    'acx-jobmgt',
    'acx-appcenter',
    'acx-jobgather',
    'acx-user',
    'acx-market',
    'acx-business',
    'ac-openapi',
    'acx-operation',
    'acx-pay',
    'acx-learning',
    'acx-authority',
]


def get_version(host, project_name):
    if project_name.startswith("sacp"):
        path = "/ac/version.html"
    elif project_name == 'easyop':
        path = "/itos/version.html"
    elif project_name == 'sso':
        path = "/sso/version.html"
    elif project_name == 'ac-openapi':
        path = "/ac/openapi/version.html"
    elif project_name == 'ac-ui':
        path = "/ac/console3/version.html"
    else:
        path = "/" + "/".join(project_name.split("-")) + "/version.html"
    res = request(url=host + path, method="get", verify=False)
    version = (res.text if res.status_code == 200 else project_name).replace("\n", "").lower().replace("snapshot-", "")
    if project_name.startswith("sacp"):
        version = version.replace("ac-", "")
    # if project_name == 'ac-openapi':
    #     version = project_name + '-' + json.loads(version).get("version")
    if not version.startswith(project_name):
        version = project_name + "-" + version
    return version


def get_versions(host):
    versions = []
    print("-------------------- %s 环境版本信息如下：--------------------" % host)
    for p in project_names:
        v = get_version(host, p)
        versions.append(v)
        print(v)
    return versions


def diff_version(host1, host2):
    host1_versions = get_versions(host1)
    host2_versions = get_versions(host2)
    print("--------------------- %s 与 %s 版本对比情况如下：------------------" % (host1, host2))
    for i in range(len(host1_versions)):
        if host1_versions[i] != host2_versions[i]:
            print(host1_versions[i], host1)
            print(host2_versions[i], host2)
            print("---------------------------------------------------------------------------------------------------")
        else:
            print(host1_versions[i] + " 版本一致！")
            print("---------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    host1 = "https://nscc.v.zzu.edu.cn"
    # host1 = "http://10.0.35.233"
    # host1 = "https://itos.sugon.com"
    # host2 = "https://ac.sugon.com"
    get_versions(host1)
    # get_versions(host2)
    # diff_version(host1, host2)
