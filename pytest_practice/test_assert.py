import pytest


# 普通断言
def test_f1():
    a = 3
    assert a % 2 == 0, "判断 a 为偶数，当前 a 的值为：%s" % a


# 断言异常
def test_zero_division_long():
    with pytest.raises(ZeroDivisionError) as excinfo1:
        a = 1 / 0

    # 断言异常类型 type
    assert excinfo1.type == ZeroDivisionError
    # 断言异常 value 值
    assert "division by zero" in str(excinfo1.value)

    with pytest.raises(ZeroDivisionError, match=".*zero.*") as excinfo2:
        a = 1 / 0


# 断言装饰器（如果有ZeroDivisionError，就XFAIL，但是属于expected failures）
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f2():
    a = 1 / 0
