# -*- coding: utf-8 -*-

import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from logs.logger import Logger
from selenium import webdriver

# 创建一个日志实例
logger = Logger(logger="BasePage").getlog()


class BasePage(object):

    # 构造函数
    def __init__(self,url, browser_type):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)


    # 调用浏览器
    def open_browser(self, browser_type):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome()
            return self.driver
        elif browser_type == 'firefox':
            self.driver = webdriver.Firefox()
            return self.driver
        else:
            print('type error')

    # 元素定位
    def find_element_and_wait(self, locator):
        """
        :param locator: 元组形式(By.ID,"id")
        :return: 返回element
        """
        element = None
        try:
            element = WebDriverWait(self.driver, 30).until(lambda driver: self.driver.find_element(*locator))
        except TimeoutException:
            # 后期改为logger
            logger.error(f"寻找{locator}元素时间超时")
            self.get_windows_img()
            # print("寻找元素时间超时")
        return element

    # 关闭
    def quit_browser(self):
        self.driver.quit()

    # 访问url
    def visit(self, url):
        self.driver.get(url)


    # 保存图片
    def get_windows_img(self):
        """
        把file_path保存到我们项目根目录的一个文件夹.\Screenshots
        """
        file_path = os.path.dirname(os.path.abspath('.')) + './Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("保存图片到文件夹 : /screenshots/")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()
