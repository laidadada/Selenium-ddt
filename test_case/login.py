# -*- coding: utf-8 -*-

from pageObject.login_page import LoginPage
from selenium import webdriver


class Login():
    driver = webdriver.Chrome()

    def login(self, driver):
        self.lg = LoginPage(driver)
        self.lg.visit(url='http://ymhtml.lecoding.cn/#/home/login')
