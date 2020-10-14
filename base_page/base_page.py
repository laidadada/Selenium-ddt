# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from logs.logger import Logger


# 创建一个日志实例
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    url = 'http://ymhtml.lecoding.cn/#/'
    page_flag_xpath = "//*[@class='el-button el-button--primary']"
    page_flag_keyword = '立即发布'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 关闭
    def quit_browser(self):
        self.driver.quit()

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 获取当前页面
    def open_and_check(self):
        self.driver.get(self.url)
        return self.check_if_page_opened()

    # 检查页面元素
    def check_if_page_opened(self):
        page_element = self.driver.find_element_by_xpath(self.page_flag_xpath)
        act_keyword = page_element.text
        if self.page_flag_keyword == act_keyword:
            print("测试通过")
            # return True

        else:
            print("测试不通过")
            # return False

    # 保存图片
    def get_windows_img(self):
        """
        把file_path保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + './Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()
