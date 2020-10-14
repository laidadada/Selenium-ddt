import unittest

from time import sleep
from web_ui.test_keywords_demo import TestKeyWords
from ddt import ddt, data, unpack


@ddt
class TestForKey(unittest.TestCase):

    # 前置条件
    def setUp(self) -> None:
        self.tk = TestKeyWords('http://www.baidu.com', 'chrome')

    # 后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()

    # 测试用例01
    @data(['id', 'test01'], ['id', 'test02'])
    @unpack
    def test_1(self, locator, input_value):
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element('id', 'su')
        sleep(2)

    # # 测试用例02
    # def test_2(self):
    #     self.tk.input_text('id', 'kw', '测试02')
    #     self.tk.click_element('id', 'su')
    #     sleep(2)


if __name__ == '__main__':
    unittest.main()
