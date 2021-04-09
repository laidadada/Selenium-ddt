# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pageObject.login_page import LoginPage


class Login(unittest.TestCase):

    def test_login_success(self):
        lg = LoginPage('http://ymhtml.lecoding.cn/#/home/login', 'firefox')
        lg.driver.maximize_window()
        lg.input_username('13977726454')
        lg.input_pwd('123456')
        lg.login_button()
        lg.driver.implicitly_wait(30)
        current_url = lg.driver.current_url
        return current_url

if __name__ == '__main__':
    unittest.main()
