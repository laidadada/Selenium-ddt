import unittest
from pageObject.login_page import LoginPage
from ddt import ddt, data, unpack
from time import sleep


@ddt
class TestLogin(unittest.TestCase, LoginPage):

    # 前置条件
    def setUp(self) -> None:
        self.lp = LoginPage(self.driver)
        self.lp.visit(url='http://ymhtml.lecoding.cn/#/home/login')

    # 后置条件
    # def tearDown(self) -> None:
    #     self.lp.quit_browser()

    @data(*[['13977726454', 'ljc960614'], ['1123123', 'Ljc960614']])
    @unpack
    # 输入正确的用户名和密码
    def test_01(self, user_name, pwd):
        self.input_username(user_name)
        self.input_pwd(pwd)
        self.login()
        sleep(5)
        self.lp.get_windows_img()
        self.check_if_page_opened()


if __name__ == '__main__':
    unittest.main()
