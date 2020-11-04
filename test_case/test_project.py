import unittest
from time import sleep

from ddt import ddt, data, unpack
from pageObject.project_page import ProjectPage
from test_case.test_login import TestLogin


@ddt
class TestPorject(unittest.TestCase):

    def setUp(self) -> None:
        self.pj = TestLogin()
        self.driver = self.pj.test_login()

    @data(['test', 'test_description', '123456', '2020-11-05', '2020-11-06'])
    @unpack
    def test_enter_my_project_and_creat_task(self, name, description, spend, start, end):

        self.empact = ProjectPage(self.driver)
        self.empact.input_Personal()
        self.empact.input_my_project()
        self.empact.input_manage_button()
        sleep(2)
        self.empact.refresh_browser()
        self.empact.input_creat_task()
        self.empact.send_task_name(name)
        self.empact.select_task_type()
        self.empact.select_task_people()
        self.empact.send_task_description(description)
        self.empact.select_task_level()
        self.empact.send_task_spend(spend)
        # self.empact.send_start_data(start)
        # self.empact.send_start_data(end)
        self.empact.input_publish()
        sleep(5)

if __name__ == '__main__':
    unittest.main()
