from base_page.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    # 搜索框元素
    input_id = (By.ID, 'kw')
    # 百度一下按钮
    click_id = (By.ID, 'su')

    def input_text(self, input_text):
        self.find_element_and_wait(self.input_id).send_keys(input_text)

    def click_element(self):
        self.find_element_and_wait(self.click_id).click()

    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    sp.check(url, 'test')
