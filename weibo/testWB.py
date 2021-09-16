import os

from Data import Data
from Opera import Login
from ddt import ddt
from ddt import data
from ddt import unpack
from unittest import TestCase
from appium import webdriver

@ddt
class TestLogin(TestCase):

    def setUp(self) -> None:
        self.vs = os.system('adb shell getprop ro.build.version.release')  # 获取手机系统版本
        # dir_path = os.path.dirname(os.path.abspath(__file__))
        # file_path = os.path.join(dir_path, 'douyinjisu.apk')    #安装包路径

        # result = os.popen("adb shell pm list package")  # 查看手机中已安装的软件包名
        # if "com.ss.android.ugc.aweme" in result.read():  # 判断此软件包名是否在手机中
        #     print("应用已安装")
        #     print('开始执行脚本>>>')
        # else:
        #     print("应用未安装,开始进行安装>>>")
        #     os.system(f'adb install {file_path}')
        # time.sleep(1)

        self.caps = {}
        self.caps["appPackage"] = "com.sina.weibo"  # 包名
        self.caps["appActivity"] = "com.sina.weibo.VisitorMainTabActivity"  # 启动名
        # caps['app'] = file_path
        self.caps["platformName"] = "Android"
        # 模拟器
        self.caps["deviceName"] = "127.0.0.1:62001"  # 设备名称
        self.caps["platformVersion"] = vs  # 安卓版本
        # 真机
        # caps["deviceName"] = "b68548ed"
        # caps["platformVersion"] = "10"
        self.caps["noReset"] = "True"  # 不初始化

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.get_h = self.driver.get_window_size()['height']  # 获取屏幕分辨率
        self.get_w = self.driver.get_window_size()['width']
    def tearDown(self) -> None:
        self.driver.quit()

    @data(*Data.testdata)
    def testLogin(self,testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = Login(self.driver)
        login.login(username,password)
        result = login.get_success_item()
        self.assertEqual(expect, result)

