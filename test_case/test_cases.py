import unittest

from selenium import webdriver
from pageObject.search_page import SearchPage
from ddt import ddt, data, unpack
from time import sleep


@ddt
class TestCases(unittest.TestCase):

    # 前置条件
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        self.sp = SearchPage(driver)

    # 后置条件
    def tearDown(self) -> None:
        self.sp.quit_browser()

    # 测试用例01
    @data(['http://www.baidu.com', 'test01'], ['http://www.baidu.com', 'test02'])
    @unpack
    def test_01(self, url, input_text):
        self.sp.check(url, input_text)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
