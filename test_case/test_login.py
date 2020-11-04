import unittest
from selenium import webdriver
from pageObject.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.lg = LoginPage(self.driver)
        self.driver.maximize_window()
        self.lg.visit(url='http://ymhtml.lecoding.cn/#/home/login')
        self.lg.input_username('17344208791')
        self.lg.input_pwd('wzl123')
        self.lg.login_button()
        self.driver.implicitly_wait(30)
        return self.driver


if __name__ == '__main__':
    unittest.main()
