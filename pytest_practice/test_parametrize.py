# -*- coding:utf-8 -*-
import pytest


ids = ["一", "二", "三"]


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)], ids=ids)
def test_eval(test_input, expected):
    print(f"测试数据{test_input},期望结果{expected}")
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6 * 9", 42, marks=pytest.mark.xfail),
    pytest.param("6*6", 42, marks=pytest.mark.skip)
])
def test_mark(test_input, expected):
    assert eval(test_input) == expected


data_1 = [1, 2, 3]
data_2 = ["a", "b"]


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    print(f'笛卡尔积 测试数据为 ： {a}，{b}')