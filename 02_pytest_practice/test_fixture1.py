# -*- coding: utf-8 -*-
import logging
import pytest

log = logging.getLogger(__name__)


@pytest.fixture
def login():
    log.info("输入账号，密码先登录")


# 调用方式一, 传入login
def test_s1(login):
    log.info("用例 1")


def test_s2():  # 不传 login
    log.info("用例 2")


@pytest.fixture
def login2():
    log.info("fixture2")


# 调用方式二：使用usefixtures，先执行login2，再执行login
@pytest.mark.usefixtures("login2", "login")
def test_s3():
    log.info("用例 3")


# 调用方式三
@pytest.fixture(autouse=True)
def login3():
    log.info("====auto===")

# autouse=True方式最先执行
# usefixtures方式谁在前先执行谁
