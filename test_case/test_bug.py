import unittest
from time import sleep

from ddt import ddt, data, unpack
from pageObject.bug_page import BugPage
from test_case.public_login import Login


@ddt
class TestBug(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Login().test_login_success()

    @data(['验证bug', '2020-11-06', '测试验证bug'])
    @unpack
    def test_insert_bug(self, title, end, description):
        self.tcb = BugPage(self.driver)
        self.tcb.input_Personal()
        self.tcb.input_my_project()
        self.tcb.input_manage_button()
        self.tcb.click_bug_list()
        self.tcb.click_add_bug()
        self.tcb.input_bug_title(title)
        self.tcb.select_module()
        self.tcb.select_task_people()
        self.driver.implicitly_wait(30)
        self.tcb.select_bug_type()
        self.driver.implicitly_wait(30)
        self.tcb.select_bug_level()
        self.driver.implicitly_wait(30)
        self.tcb.select_bug_vesrion()
        self.tcb.send_bug_end_data(end)
        self.tcb.send_bug_description(description)
        self.tcb.submit()


if __name__ == '__main__':
    unittest.main()
