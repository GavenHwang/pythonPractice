# -*- coding: utf-8 -*-
from unittest import mock

from jsonpath import jsonpath

result1 = mock.Mock(name='mock名称')
print(result1)
mock_value1 = mock.Mock(return_value="返回值1")
print(mock_value1())
mock_value2 = mock.Mock(return_value="返回值2", side_effect=[1, 2, 3])
print(mock_value2())
print(mock_value2())
print(mock_value2())

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
