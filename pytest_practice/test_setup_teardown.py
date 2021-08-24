# -*- coding: utf-8 -*-
import logging

import pytest
log = logging.getLogger(__file__)


def setup_module():
    log.info("=====整个.py模块开始前只执行一次:打开浏览器=====")


def teardown_module():
    log.info("=====整个.py模块结束后只执行一次:关闭浏览器=====")


def setup_function():
    log.info("===每个函数级别用例开始前都执行setup_function===")


def teardown_function():
    log.info("===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    log.info("one")


def test_two():
    log.info("two")


class TestCase:
    def setup(self):
        log.info("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        log.info("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        log.info("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        log.info("==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        log.info("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        log.info("=类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        log.info("three")