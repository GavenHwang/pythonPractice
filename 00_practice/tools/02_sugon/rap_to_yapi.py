# -*- coding:utf-8 -*-
import json
import os
import re

import requests


def login_rap(username, password):
    """登录rap，获得cookie"""
    res1 = requests.post(url="http://10.0.35.17/org/index.do")
    cookie1 = res1.cookies.get_dict()
    requests.post(url="http://10.0.35.17/account/doLogin.do", data={"account": username, "password": password},
                  headers={"Cookie": "JSESSIONID=%s" % cookie1.get("JSESSIONID"),
                           "Content-Type": "application/x-www-form-urlencoded",
                           "Upgrade-Insecure-Requests": "1"})
    return cookie1


def get_project_ids(project_line, base_url, cookie):
    """获取产品线下的所有项目"""
    projects = []
    res = requests.post(base_url, cookies=cookie)
    result = res.json()
    for group in result.get("groups"):
        for project in group.get("projects"):
            projects.append({
                "project_line": project_line,
                "group": group.get("name"),
                "name": project.get("name"),
                "id": project.get("id")
            })
    return projects


def suggest_action_file_name(request_url):
    url_split = request_url.split("/")
    url_split.reverse()
    action_file_name = url_split[0].split("?")[0].split(".")[0].strip()
    if "{" in action_file_name or "}" in action_file_name:
        for url in url_split[1:]:
            action_file_name = str("%s_%s" % (url, action_file_name)).replace("{", "").replace("}", "")
            if "{" not in url and "}" not in url:
                break
    return action_file_name


requestTypeDict = {
    "1": "GET",
    "2": "POST",
    "3": "PUT",
    "4": "DELETE",
}


def get_rap_project_json_and_save_as_jsonfile(projects):
    for project in projects:
        yapi_json = []
        project_id = project.get("id")
        project_url = "http://10.0.35.17/api/queryRAPModel.do?projectId=%s" % project_id
        res = requests.post(project_url)
        res_json_obj = res.json()
        # 去掉空白字符和多余的转移反斜杠"\"
        pattern = re.compile(r'\s+')
        modelJSON = re.sub(pattern, '', res_json_obj["modelJSON"].replace("\\\'", "\'"))
        modelJSON_list = json.loads(modelJSON)["moduleList"]
        modelJSON_list.sort(key=lambda item: item['name'])
        # 遍历各个项目模块下的接口，保存为yaml
        for modelJSON in modelJSON_list:
            model_name = modelJSON["name"].replace(" ", "").replace("/", "_")
            model_json = {
                "index": 0,
                "name": model_name,
                "desc": model_name,
                "list": []
            }
            pageList = modelJSON["pageList"]
            for page in pageList:
                page_name = page["name"].replace(" ", "").replace("/", "_")
                actionList = page["actionList"]
                index = 0
                for action in actionList:
                    path = "/" + "/".join(action.get("requestUrl", "").replace("://", "").split("/")[1:])
                    if "getCurrentUserInfo" in path:
                        print("debug")
                    if "?" in path:
                        path = path.split("?")[0]
                    # 请求参数
                    action_type = requestTypeDict.get(action.get("requestType"))
                    if action_type == "GET":
                        requestParameter = []
                        for req_param in action.get("requestParameterList"):
                            requestParameter.append({
                                "name": req_param.get("identifier"),
                                "desc": req_param.get("name"),
                                "required": "1" if "不能为空" in req_param.get("remark") else "0"
                            })
                    else:
                        requestParameter = {"type": "object", "title": "empty object", "properties": {}}
                        required = []
                        for req_param in action.get("requestParameterList"):
                            requestParameter["properties"][req_param.get("identifier")] = {
                                "type": req_param.get("dataType"),
                                "mock": {},
                                "description": req_param.get("name")
                            }
                            if "不能为空" in req_param.get("remark") or "不可为空" in req_param.get("remark") or \
                                    "非空" in req_param.get("remark"):
                                required.append(req_param.get("identifier"))

                            if req_param.get("parameterList"):
                                requestParameter["properties"][req_param.get("identifier")]["properties"] = {}
                                for d in req_param.get("parameterList"):
                                    requestParameter["properties"][req_param.get("identifier")]["properties"][
                                        d.get("identifier")] = {
                                        "type": d.get("dataType"),
                                        "mock": {},
                                        "description": d.get("name")
                                    }
                        requestParameter["required"] = required
                        requestParameter = json.dumps(requestParameter)
                    responseParameter = {"type": "object", "title": "empty object", "properties": {}, "required": []}
                    for res_param in action.get("responseParameterList"):
                        responseParameter["properties"][res_param.get("identifier")] = {
                            "type": res_param.get("dataType"),
                            "mock": {},
                            "description": res_param.get("name"),
                        }
                        if res_param.get("parameterList"):
                            responseParameter["properties"][res_param.get("identifier")]["properties"] = {}
                            for d in res_param.get("parameterList"):
                                responseParameter["properties"][res_param.get("identifier")]["properties"][
                                    d.get("identifier")] = {
                                    "type": d.get("dataType"),
                                    "mock": {},
                                    "description": d.get("name")
                                }
                    responseParameter = json.dumps(responseParameter)
                    action = {
                        "query_path": {
                            "path": path,
                            "params": []
                        },
                        "edit_uid": 0,
                        "status": "done",
                        "type": "static",
                        "req_body_is_json_schema": True,
                        "res_body_is_json_schema": True,
                        "api_opened": False,
                        "index": index,
                        "tag": [model_name, page_name],
                        "method": action_type,
                        "title": "%s-%s" % (page_name, action.get("name")),
                        "path": path,
                        "req_headers": [],
                        "req_params": [],
                        "req_body_form": [],
                        "req_body_type": "json",
                        "req_query": requestParameter if action_type == "GET" else [],
                        "req_body_other": requestParameter if action_type != "GET" else "",
                        "res_body_type": "json",
                        "res_body": responseParameter,
                        "__v": 0,
                        "desc": action.get("description", "").replace("br>", "p>"),
                        "markdown": action.get("description", "").replace("<br>", "").replace("</br>", ""),
                    }
                    model_json["list"].append(action)
                    index += 1
            yapi_json.append(model_json)
        project_path = os.path.join(project.get("project_line"), project.get("group"), project.get("name"))
        os.makedirs(project_path, exist_ok=True)
        project_json_file_name = os.path.join(project_path, "%s-%s-%s.json" % (
            project.get("project_line"), project.get("group"), project.get("name")))
        with open(project_json_file_name, "w") as f:
            json.dump(yapi_json, f)


if __name__ == "__main__":
    cookie = login_rap("huangleilei", "sugon.")
    ac_product_line_url = "http://10.0.35.17/org/group/all.do?productlineId=1"
    gv_product_line_url = "http://10.0.35.17/org/group/all.do?productlineId=3"
    ai_product_line_url = "http://10.0.35.17/org/group/all.do?productlineId=5"
    ac_projects = get_project_ids('AC', ac_product_line_url, cookie)
    gv_projects = get_project_ids('Gridview', gv_product_line_url, cookie)
    ai_projects = get_project_ids('SothisAi', ai_product_line_url, cookie)
    get_rap_project_json_and_save_as_jsonfile(ac_projects)
    get_rap_project_json_and_save_as_jsonfile(gv_projects)
    get_rap_project_json_and_save_as_jsonfile(ai_projects)
