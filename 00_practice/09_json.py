# -*- coding:utf-8 -*-
import json

from jsonpath import jsonpath

res = {
    "code": 0,
    "msg": "OK",
    "data": [
        {
            "token_info": {
                "token_type": "Bearer",
                "expires_in": "2020-05-28 13:07:29",
                "token": "eyJhbGciOiJIUzUxAiJ9.eyJtZW1iZZJfaWQiOjEwMDA1MTMxNSwiZXhwIjoxNTkwNjQyNDQ5fQ.s6A7pzLILf9tqpEDAU9wIPGGLGkgKEQ6EBHq26l-eUM5seCb48DWalkE7u16iRZv3uzD5hIDFbw41Jmi9V0T_Q"
            }
        },
        {
            "token_info": {
                "token_type": "Bearer",
                "expires_in": "2020-05-28 13:07:29",
                "token": "AAJhbGciOiJIUzUxAiJ9.eyJtZW1iZZJfaWQiOjEwMDA1MTMxNSwiZXhwIjoxNTkwNjQyNDQ5fQ.s6A7pzLILf9tqpEDAU9wIPGGLGkgKEQ6EBHq26l-eUM5seCb48DWalkE7u16iRZv3uzD5hIDFbw41Jmi9V0T_Q"
            }
        }
    ]
}
token = jsonpath(res, '$.data[1].token_info.token')[0]
print(token)

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
print(js)
