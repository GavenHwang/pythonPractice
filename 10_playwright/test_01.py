from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://itos2.sugon.com/")
    page.goto("https://itos2.sugon.com/ac/home/index.html")
    page.get_by_role("link", name="登录").click()
    page.get_by_placeholder("用户名/邮箱/手机号").click()
    page.get_by_placeholder("用户名/邮箱/手机号").fill("api_leader_01")
    page.get_by_placeholder("用户名/邮箱/手机号").press("Tab")
    page.get_by_placeholder("密码").fill("111111a")
    page.get_by_placeholder("密码").press("Enter")
    page.get_by_role("button", name="确定").click()
    page.get_by_text("退出", exact=True).click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
