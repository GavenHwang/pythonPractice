# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver


class TestCase1:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        self.driver.find_element_by_id('kw').send_keys("selenium")
        sleep(3)
        self.driver.find_element_by_id('su').click()
        sleep(10)
        self.driver.quit()

    def test2(self):
        import subprocess
        p = subprocess.Popen("chromedriver")
        p.communicate()


if __name__ == '__main__':
    TestCase1().test()
    # TestCase1().test2()