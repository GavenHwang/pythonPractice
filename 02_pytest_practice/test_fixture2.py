# -*- coding: utf-8 -*-
import logging
import pytest

log = logging.getLogger(__name__)
order = []


@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3, a1):
    # 先实例化f3, 再实例化a1, 最后实例化f1
    order.append("f1")
    assert f3 == 123


@pytest.fixture
def f3():
    order.append("f3")
    a = 123
    yield a


@pytest.fixture
def a1():
    order.append("a1")


@pytest.fixture
def f2():
    order.append("f2")


def test_order(f1, m1, f2, s1):
    # 虽然m1、s1在f1后，但因为scope范围大，所以会优先实例化
    assert order == ["s1", "m1", "f3", "a1", "f1", "f2"]


# ------------------------------------------------------------------------
@pytest.fixture(scope="session")
def open():
    log.info("===打开浏览器===")


@pytest.fixture
# @pytest.mark.usefixtures("open") 不可取！！！不生效！！！
def login(open):
    # 方法级别前置操作setup
    log.info(f"输入账号，密码先登录{open}")