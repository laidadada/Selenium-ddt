from base_page.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    login_name = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div[2]/input")
    login_pwd = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[3]/div/input")
    login_button = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[5]/button')

    def input_username(self, user_name):
        self.locator(self.login_name).send_keys(user_name)

    def input_pwd(self, pwd):
        self.locator(self.login_pwd).send_keys(pwd)

    def login(self):
        self.locator(self.login_button).click()

