# -*- coding: utf-8 -*-
from selenium import webdriver

from pageObject.login_page import LoginPage
from ddt import ddt, data, unpack
from logs.logger import Logger

# 创建一个日志实例
logger = Logger(logger='TestLogin').getlog()

@ddt()
class PublicLogin(LoginPage):

    # 前置条件
    def setUp(self) -> None:
        self.lp = LoginPage(self.driver)
        logger.info('打开猿盟网站')
        self.lp.visit(url='http://ymhtml.lecoding.cn/#/home/login')

    @data(*[['13977726454', 'ljc960614']])
    @unpack
    # 输入正确的用户名和密码
    def test_01(self, user_name, pwd):
        logger.info('输入用户名： ' + user_name)
        self.input_username(user_name)
        logger.info('输入密码： ' + pwd)
        self.input_pwd(pwd)
        logger.info('点击登录按钮')
        self.login()
