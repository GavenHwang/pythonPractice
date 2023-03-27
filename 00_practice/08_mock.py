# -*- coding:utf-8 -*-
from unittest import mock

result1 = mock.Mock(name='mock名称')
print(result1)
mock_value1 = mock.Mock(return_value="返回值1")
print(mock_value1())
mock_value2 = mock.Mock(return_value="返回值2", side_effect=[1, 2, 3])
print(mock_value2())
print(mock_value2())
print(mock_value2())
