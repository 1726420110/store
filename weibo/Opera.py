# 第一次安装软件运行可能有弹窗，请在次运行即可。
# 已经适配不同版本的安卓手机和分辨率
from appium import webdriver
import time
import os

from appium.webdriver.common.touch_action import TouchAction


class Login:
    #  初始化全局方法
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element_by_id("com.sina.weibo:id/titleBack").click()
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_phone").send_keys(username)
        self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()
        self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_resent").click()
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_sms").send_keys(password)
        TouchAction(self.driver).tap(x=417, y=528).perform()

    def get_success_item(self):
        if self.driver.find_element_by_id("com.sina.weibo:id/titleBack"):
            return 1
