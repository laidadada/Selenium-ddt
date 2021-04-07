# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from base_page.base_page import BasePage


class BugPage(BasePage):
    personal = (By.XPATH, "//*[@id='head']/div/div[4]")
    my_project = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div/a[2]")
    manage_button = (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div/div[2]/button')
    bug_list = (By.XPATH, '//*[@class="project_tab"]/a[5]')
    add_bug = (By.XPATH, '//*[@class="el-button el-button--primary"]')
    bug_title = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/input')
    module = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[3]/div/div/div/input')
    module01 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    task_people = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[4]/div/div/div[1]/input')
    task_people01 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
    bug_type = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[5]/div/div/div[1]/input')
    bug_type01 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    bug_level = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[6]/div/div/div[1]/input')
    bug_level01 = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
    bug_vesrion = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[7]/div/div/div/input')
    bug_vesrion01 = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
    bug_end_data = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[8]/div/div/input')
    bug_description = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[9]/div/div[1]/div[2]/div[1]')
    submit = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[10]/button[1]')

    # 个人中心
    def input_Personal(self):
        self.find_element_and_wait(self.personal).click()

    # 我的项目
    def input_my_project(self):
        self.find_element_and_wait(self.my_project).click()

    # 点击管理
    def input_manage_button(self):
        self.find_element_and_wait(self.manage_button).click()

    # 点击bug列表
    def click_bug_list(self):
        self.find_element_and_wait(self.bug_list).click()

    # 点击添加bug
    def click_add_bug(self):
        self.find_element_and_wait(self.add_bug).click()

    # 输入bug标题
    def input_bug_title(self, title):
        self.find_element_and_wait(self.bug_title).send_keys(title)

    # 选择所属板块
    def select_module(self):
        self.find_element_and_wait(self.module).click()
        self.find_element_and_wait(self.module01).click()

    # 选择指派人员
    def select_task_people(self):
        self.find_element_and_wait(self.task_people).click()
        self.find_element_and_wait(self.task_people01).click()

    # 选择Bug类型
    def select_bug_type(self):
        self.find_element_and_wait(self.bug_type).click()
        self.find_element_and_wait(self.bug_type01).click()

    # 选择Bug级别
    def select_bug_level(self):
        self.find_element_and_wait(self.bug_level).click()
        self.find_element_and_wait(self.bug_level01).click()

    # 选择Bug版本
    def select_bug_vesrion(self):
        self.find_element_and_wait(self.bug_vesrion).click()
        self.find_element_and_wait(self.bug_vesrion01).click()

    # 选择日期: 结束时间
    def send_bug_end_data(self, end):
        self.find_element_and_wait(self.bug_end_data).send_keys(end)

    # 输入重现步骤
    def send_bug_description(self, description):
        self.find_element_and_wait(self.bug_description).send_keys(description)

    # 提交
    def submit_button(self):
        self.find_element_and_wait(self.submit).click()
