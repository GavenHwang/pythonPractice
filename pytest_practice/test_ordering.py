# -*- coding: utf-8 -*-
import logging
import pytest

log = logging.getLogger(__file__)


@pytest.mark.run(order=1)
def test_01():
    log.info('test01')


@pytest.mark.run(order=2)
def test_02():
    log.info('test02')


@pytest.mark.last
def test_05():
    log.info('test05')


def test_04():
    log.info('test04')


@pytest.mark.run(order=3)
def test_03():
    log.info('test03')