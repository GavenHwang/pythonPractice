# -*- coding:utf-8 -*-
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 启动 chromium 浏览器, 默认是无头浏览器模式，即：headless=True; slow_mo开启慢速模式，每个操作间增加1毫秒的时间间隔
    browser = p.chromium.launch(headless=False, slow_mo=1)
    page = browser.new_page()  # 打开一个标签页
    page.goto("https://www.baidu.com")  # 打开百度地址
    print(page.title())  # 打印当前页面title
    page.wait_for_timeout(1000)  # 默认会自动等待，如果调试需要，应该使用 page.wait_for_timeout(1000) 代替：time.sleep(1)
    # Selector选择器 ----------------------------------------------------------------------------------------------------
    # 1. 先定位再操作
    # page.locator('#kw').fill("playwright中文文档")
    # page.locator('#su').click()
    # 2. 传Selector选择器，直接操作（推荐）
    page.fill('#kw', "playwright中文文档")
    # page.click('#su')
    # 3. CSS and XPath
    # page.fill('css=#kw', "playwright中文文档")
    # page.click('xpath=//*[@id="su"]')
    # 4. XPath 和 CSS 选择器可以绑定到 DOM 结构或实现。
    # 当 DOM 结构发生变化时，这些选择器可能会中断。下面的长 CSS 或 XPath 链是导致测试不稳定的不良做法的示例：
    # page.click("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
    # page.click('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    # text 文本选择器 ---------------------------------------------------------------------------------------------------
    # xpath选择器，完全匹配文本 //*[text() = "playwright"]
    # xpath选择器，包含某个文本 //*[contains(text(), "playwright")]
    # page.click("text=贴吧", timeout=3000)  # 没有引号，模糊匹配，对大小写不敏感
    # page.click("text='知道'", timeout=3000)  # 有引号，精确匹配，对大小写敏感
    page.click('text=百度一下')
    # Selector 选择器组合定位 --------------------------------------------------------------------------------------------
    page.click('text=登录')
    # id 属性+ css
    page.fill('form >> [name="userName"]', "tom")
    # page.locator("form").locator('[name="username"]').fill("17630503786")
    page.fill('#TANGRAM__PSP_11__password', "123456")
    page.click("#TANGRAM__PSP_11__submitWrapper >> text=登录")
    # 内置定位器 --------------------------------------------------------------------------------------------------------
    # page.get_by_role()            通过显式和隐式可访问性属性进行定位
    # page.get_by_text()            通过文本内容定位
    # page.get_by_label()           通过关联标签的文本定位表单控件
    # page.get_by_placeholder()     按占位符定位输入
    # page.get_by_alt_text()        通过替代文本定位元素，通常是图像
    # page.get_by_title()           通过标题属性定位元素
    # page.get_by_test_id()         根据data-testid属性定位元素（可以配置其他属性）
    # 示例:
    # page.get_by_label("User Name").fill("John")
    # page.get_by_label("Password").fill("secret-password")
    # page.get_by_role("button", name="Sign in").click()
    # expect(page.get_by_text("Welcome, John!")).to_be_visible()
    #
    # 角色定位 page.get_by_role() ---------------------------------------------------------------------------------------
    # locator = page.get_by_role("button", name="Sign in")
    # locator.hover()   # 在每个动作之前，定位器重新对应新元素
    # locator.click()
    #
    # 多重定位
    # locator = page.frame_locator("my-frame").get_by_role("button", name="Sign in")
    # locator.click()
    #
    # expect(page.get_by_role("heading", name="Sign up")).to_be_visible()
    # page.get_by_role("checkbox", name="Subscribe").check()
    # page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
    #
    # 输入框标签 page.get_by_label() ------------------------------------------------------------------------------------
    # page.get_by_role("button", name="Sign in").click()
    # locator = page.get_by_role("button", name="Sign in")
    # locator.hover()
    # locator.click()
    #
    # locator = page.frame_locator("my-frame").get_by_role("button", name="Sign in")
    # locator.click()
    #
    # expect(page.get_by_role("heading", name="Sign up")).to_be_visible()
    # page.get_by_role("checkbox", name="Subscribe").check()
    # page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
    #
    # 输入框标签 page.get_by_label() ------------------------------------------------------------------------------------
    # page.get_by_label("Password").fill("secret")
    #
    # 输入框 page.get_by_placeholder() ---------------------------------------------------------------------------------
    # page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
    #
    # 包含的文本 page.get_by_text() -------------------------------------------------------------------------------------
    # expect(page.get_by_text("Welcome, John")).to_be_visible()
    # expect(page.get_by_text("Welcome, John", exact=True)).to_be_visible() # 精确匹配
    # expect(page.get_by_text(re.compile("welcome, john", re.IGNORECASE))).to_be_visible()
    #
    # 包含的文本 page.get_by_text() -------------------------------------------------------------------------------------
    # page.get_by_alt_text("playwright logo").click()
    #
    # title 属性 page.get_by_title() -----------------------------------------------------------------------------------
    # expect(page.get_by_title("Issues count")).to_have_text("25 issues")
    #
    # 测试 ID page.get_by_test_id() ------------------------------------------------------------------------------------
    # page.get_by_test_id("directions").click()
    # playwright.selectors.set_test_id_attribute("data-pw")
    # page.get_by_test_id("directions").click()
    browser.close()  # 关闭浏览器对象
