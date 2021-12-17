import pytest


# # 普通断言
# def test_f1():
#     a = 3
#     assert a % 2 == 0, "判断 a 为偶数，当前 a 的值为：%s" % a
#
#
# # 断言异常
# def test_zero_division_long():
#     with pytest.raises(ZeroDivisionError) as excinfo1:
#         a = 1 / 0
#
#     # 断言异常类型 type
#     assert excinfo1.type == ZeroDivisionError
#     # 断言异常 value 值
#     assert "division by zero" in str(excinfo1.value)
#
#     with pytest.raises(ZeroDivisionError, match=".*zero.*") as excinfo2:
#         a = 1 / 0
#
#
# # 断言装饰器（如果有ZeroDivisionError，就XFAIL，但是属于expected failures）
# @pytest.mark.xfail(raises=ZeroDivisionError)
# def test_f2():
#     a = 1 / 0
from assertpy import assert_that
from pytest_assume.plugin import assume

def fun_assume():
    for i in range(2):
        with assume:
            assert_that(i).is_equal_to(2)
        with assume:
            assert_that(i).is_equal_to(22)

res_json = {'code': '612017', 'data': '', 'msg': 'no privilege to access assistant '}
request_data = {'expect_key_code': 'code', 'expect_key_msg': 'msg', 'expect_value_code': '0', 'expect_value_msg': 'success'}
def test_assume():
    fun_assume()
    base_res_json_assert(res_json, request_data)

def base_res_json_assert(res_json, request_data, with_assume=True):
    """
    request_data = {
        'expect_key_code': 'code',
        'expect_value_code': '0',
        'expect_key_msg': 'msg',
        'expect_value_msg': 'success'
    }
    该方法实现的效果相当于：
    with assume:
        assert_that(res_json).contains_key("code")
    with assume:
        assert_that(res_json["code"]).is_equal_to("0")
    with assume:
        assert_that(res_json).contains_key("msg")
    with assume:
        assert_that(res_json["code"]).is_equal_to("success")
    """
    request_keys = list(request_data.keys())
    for k in request_keys:
        if k.startswith("expect_key_"):
            code = k.replace("expect_key_", "")
            if with_assume:
                with assume:
                    assert_that(res_json).contains_key(request_data[k])
            else:
                assert_that(res_json).contains_key(request_data[k])
            k_value = "expect_value_%s" % code
            if k_value in request_keys:
                if with_assume:
                    if code == 'code':
                        with assume:
                            assert_that(res_json[request_data[k]]).is_equal_to(request_data[k_value])
                    else:
                        with assume:
                            assert_that(res_json[request_data[k]]).contains(request_data[k_value])
                else:
                    if code == 'code':
                        assert_that(res_json[request_data[k]]).is_equal_to(request_data[k_value])
                    else:
                        assert_that(res_json[request_data[k]]).contains(request_data[k_value])