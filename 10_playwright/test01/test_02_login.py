# -*- coding:utf-8 -*-
import pytest
from playwright.sync_api import Page, expect





def test_example(page: Page) -> None:
    page.goto("https://itos2.sugon.com/")
    page.goto("https://itos2.sugon.com/ac/home/index.html")
    page.get_by_role("link", name="登录").click()
    page.get_by_placeholder("用户名/邮箱/手机号").click()
    page.get_by_placeholder("用户名/邮箱/手机号").fill("api_leader_01")
    page.get_by_placeholder("用户名/邮箱/手机号").press("Tab")
    page.get_by_placeholder("密码").fill("111111a")
    page.get_by_placeholder("密码").press("Enter")
    if page.get_by_role("button", name="确定").count():
        page.get_by_role("button", name="确定").click()
    page.get_by_text("退出", exact=True).click()

