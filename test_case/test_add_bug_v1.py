import unittest
from pageObject.login_page import LoginPage
from config.public_login import Login


class MyTestCase(unittest.TestCase):

    def setUp(self):
        lg = LoginPage('http://ymhtml.lecoding.cn/#/home/login', 'firefox')
        lg.driver.maximize_window()
        lg.input_username('17740500814')
        lg.input_pwd('123456')
        lg.login_button()
        lg.driver.implicitly_wait(30)

    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
