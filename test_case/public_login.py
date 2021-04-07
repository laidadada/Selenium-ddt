# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pageObject.login_page import LoginPage


class Login(unittest.TestCase):

    def test_login_success(self):
        self.driver = webdriver.Firefox()
        lg = LoginPage(self.driver)
        self.driver.maximize_window()
        lg.visit(url='http://ymhtml.lecoding.cn/#/home/login')
        lg.input_username('13977726454')
        lg.input_pwd('123456')
        lg.login_button()
        self.driver.implicitly_wait(30)
        return self.driver


if __name__ == '__main__':
    unittest.main()
