import pytest
from pageObject.login_page import LoginPage
from config.yamlload import loadyaml

class TestLoginV1:

    def setup_class(self):
        self.bg = LoginPage('http://ymhtml.lecoding.cn/#/home/login', 'firefox')
        self.bg.driver.maximize_window()

    @pytest.mark.parametrize('data', loadyaml('../Cases_data/login_datas.yaml'))
    def test_login(self, data):
        self.bg.input_username(data['username'])
        self.bg.input_pwd(data['password'])
        self.bg.login_button()
        self.bg.driver.implicitly_wait(20)
        info_message = self.bg.driver.find_element_by_xpath("//*[@class = 'el-message el-message--success']").text
        if info_message == u'登录成功，即将跳转首页':
            print('测试结果： 用例通过')
        else:
            print('测试结果： 用例不通过')
            self.bg.get_windows_img()

    def tearDown_class(self):
        self.bg.quit_browser()

if __name__ == '__main__':
    pytest.main(['-s','-v', 'test_login_v1.py'])