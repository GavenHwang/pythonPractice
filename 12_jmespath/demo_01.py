import jmespath

data = [
    {"url": "http:\/\/10.21.52.1:7095", "version": "", "enable": "false"},
    {"url": "http:\/\/111.11.100.223:58009", "version": "", "nodeName": "", "appId": "", "udpPort": "", "appSecret": "",
     "fastTransEnable": "false", "isManagerNode": "false", "enable": "true"}
]
# 获取键值对值
search_cond = "[?enable=='true'] | url"
res = jmespath.search(search_cond, data)
print(res)

data = {
    "name": "张三",
    "age": 26,
    "gender": "男",
    "grade": {
        "Chinese": 996,
        "Math": 999,
        "English": {
            "a": 1,
            "b": 2,
        }
    },
    "records": [
        {
            "Chinese": 95,
            "Math": 100
        },
        {
            "Chinese": 98,
            "Math": 98
        },
        {
            "Chinese": 96,
            "Math": 100
        },
        {
            "Chinese": 97,
            "Math": 98,
            "b": [1, 2, 3]
        },
    ]
}

# 获取键值对值
search_cond = '{NAME:name, AGE:age, RECORDS:records}'
res = jmespath.search(search_cond, data)
print(res)

# 获取对象值
search_name = 'name'
res_name = jmespath.search(search_name, data)
print(res_name)

# 使用子表达式获取值，若值不存在返回null
search_sub_value = 'grade.Chinese'
res_sub_value = jmespath.search(search_sub_value, data)
print(res_sub_value)

# 列表取值,索引从0开始，若是
search_list1 = 'records[1].Chinese'
res_list1 = jmespath.search(search_list1, data)
print(res_list1)

ret1 = jmespath.search("records[0:1]", data)
print(ret1)

ret1 = jmespath.search("records[::2]", data)
print(ret1)

# 列表投影
ret1 = jmespath.search("records[*]", data)
print(ret1)

ret1 = jmespath.search("records[*].Math", data)
print(ret1)

ret1 = jmespath.search("records[:2].Math", data)
print(ret1)

# 对象投影
ret1 = jmespath.search("grade.*", data)
print(ret1)

ret1 = jmespath.search("grade.*.a", data)
print(ret1)

ret1 = jmespath.search("records[*].b[*]", data)
print(ret1)

data = {
    "book": [
        {"name": "a1", "author": "aa"},
        {"name": "a2", "author": "aa"},
        {"name": "b", "author": "bb"}
    ]
}

ret1 = jmespath.search("book[?author=='aa'].name", data)
print(ret1)

ret2 = jmespath.search("book[*].name | [1]", data)
print(ret2)

data = {
    "people": [
        {
            "name": "a",
            "state": {"name": "up"}
        },
        {
            "name": "b",
            "state": {"name": "down"}
        },
        {
            "name": "c",
            "state": {"name": "up"}
        }
    ]
}

ret = jmespath.search("people[].[name, state.name]", data)
print(ret)

data = {
    "people": [
        {
            "name": "a",
            "state": {"name": "up"}
        },
        {
            "name": "b",
            "state": {"name": "down"}
        },
        {
            "name": "c",
            "state": {"name": "up"}
        }
    ]
}

ret = jmespath.search("people[].[name, state.name]", data)
print(ret)

ret = jmespath.search("people[].{name: name, state_name: state.name}", data)
print(ret)

data = {
    "name": ['张三', '李四', '张三丰', '王五']
}

ret = jmespath.search("name[?contains(@, '张')]", data)
print(ret)

data = {
    "people": [{"name": "张三", 'age': 25}, {"name": "李四", 'age': 26}, {"name": "王五", 'age': 23}]
}

ret = jmespath.search("sort_by(people, &age)", data)
print(ret)

data = {
    "a": [
        {
            "b": [
                {"name": "a"},
                {"name": "b"}
            ]
        },
        {
            "b": [
                {"name": "c"},
                {"name": "d"}
            ]
        }
    ]
}

ret1 = jmespath.search("a[*].b[*].name", data)
print(ret1)

ret2 = jmespath.search("a[*].b[].name", data)
print(ret2)

ret3 = jmespath.search("a[].b[].name", data)
print(ret3)

ret4 = jmespath.search("a[].b[*].name", data)
print(ret4)

ret5 = jmespath.search("a[].b[]", data)
print(ret5)
