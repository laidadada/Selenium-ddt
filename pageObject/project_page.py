# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from base_page.base_page import BasePage


class ProjectPage(BasePage):
    personal = (By.XPATH, "//*[@id='head']/div/div[4]")
    my_project = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div/a[2]")
    manage_button = (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div/div[2]/button')
    task_list = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div/a[2]')
    creat_task = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div/button[1]')
    task_name = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div/div/input')
    task_type = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div/div/div/input')
    task_type01 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    task_people = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[4]/div/div/div[1]/input')
    task_people01 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
    task_description = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[5]/div/div[1]/div[2]/div[1]')
    task_level = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[6]/div/div/div/input')
    task_level01 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')
    task_spend = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[7]/div/div/input')
    data = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[8]/div/div/input[1]')
    start_data = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[8]/div/div[1]/input')
    end_data = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[8]/div/div[2]/input')
    publish = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[12]/button[1]')

    # 个人中心
    def input_Personal(self):
        self.find_element_and_wait(self.personal).click()

    # 我的项目
    def input_my_project(self):
        self.find_element_and_wait(self.my_project).click()

    # 点击管理
    def input_manage_button(self):
        self.find_element_and_wait(self.manage_button).click()

    # 点击任务列表
    def input_task_list(self):
        self.find_element_and_wait(self.task_list).click()

    # 点击创建任务
    def input_creat_task(self):
        self.find_element_and_wait(self.creat_task).click()

    # 输入任务名称
    def send_task_name(self, name):
        self.find_element_and_wait(self.task_name).send_keys(name)

    # 选择任务类型
    def select_task_type(self):
        self.find_element_and_wait(self.task_type).click()
        self.find_element_and_wait(self.task_type01).click()

    # 选择指派人员
    def select_task_people(self):
        self.find_element_and_wait(self.task_people).click()
        self.find_element_and_wait(self.task_people01).click()

    # 输入任务描述
    def send_task_description(self, description):
        self.find_element_and_wait(self.task_description).send_keys(description)

    # 选择任务等级
    def select_task_level(self):
        self.find_element_and_wait(self.task_level).click()
        self.find_element_and_wait(self.task_level01).click()

    # 输入任务花费
    def send_task_spend(self, spend):
        self.find_element_and_wait(self.task_spend).send_keys(spend)

    # 选择日期: 开始时间
    def send_start_data(self, start):
        self.find_element_and_wait(self.start_data).send_keys(start)

    # 选择日期: 结束时间
    def send_end_data(self, end):
        self.find_element_and_wait(self.end_data).send_keys(end)

    # 发布当前任务
    def input_publish(self):
        self.find_element_and_wait(self.publish).click()
