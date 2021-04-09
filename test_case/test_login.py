# -*- coding: utf-8 -*-
import unittest
from time import sleep
from ddt import ddt, data, unpack
from pageObject.login_page import LoginPage

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        print('测试开始')
        self.bg = LoginPage('http://ymhtml.lecoding.cn/#/home/login', 'firefox')
        self.bg.driver.maximize_window()

    @data(['17740500814','123456'])
    @unpack
    def test_login_01(self, username, password):
        self.bg.input_username(username)
        self.bg.input_pwd(password)
        self.bg.login_button()
        self.bg.driver.implicitly_wait(20)
        info_message = self.bg.driver.find_element_by_xpath("//*[@class = 'el-message el-message--success']").text
        if info_message == u'登录成功，即将跳转首页':
            print('测试结果： 用例通过')
        else:
            print('测试结果： 用例不通过')
            self.bg.get_windows_img()

    def tearDown(self):
        self.bg.quit_browser()




if __name__ == '__main__':
    unittest.main()
