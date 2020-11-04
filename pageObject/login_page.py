
from selenium.webdriver.common.by import By
from base_page.base_page import BasePage


class LoginPage(BasePage):

    login_name = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div[2]/input")
    login_pwd = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[3]/div/input")
    login_buttons = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[5]/button')

    def input_username(self, user_name):
        self.find_element_and_wait(self.login_name).send_keys(user_name)

    def input_pwd(self, pwd):
        self.find_element_and_wait(self.login_pwd).send_keys(pwd)

    def login_button(self):
        self.find_element_and_wait(self.login_buttons).click()

