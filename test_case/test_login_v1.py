import pytest
from pageObject.login_page import LoginPage
from config.yamlload import loadyaml

class TestLoginV1:

    def setup_class(self):
        self.bg = LoginPage('http://ymhtml.lecoding.cn/#/home/login', 'firefox')
        self.bg.driver.maximize_window()

    def teardown_class(self):
        self.bg.quit_browser()

    @pytest.mark.parametrize('data', loadyaml('../Cases_data/login_datas.yaml'))
    def test_login(self, data):
        self.bg.input_username(data['username'])
        self.bg.input_pwd(data['password'])
        self.bg.login_button()
        self.bg.driver.implicitly_wait(20)
        info_message = self.bg.driver.find_element_by_xpath("//*[@class = 'el-message el-message--success']").text
        try:
            assert info_message == u'登录成功，即将跳转首页'
            print(" 结束执行 {0} 测试用例， 测试结果 --- PASS ")
            self.bg.get_windows_img()
        except:
            print(" 结束执行 {0} 测试用例， 测试结果 --- False ")
            self.bg.get_windows_img()
            raise

if __name__ == '__main__':
    pytest.main(['-s','-v', 'test_login_v1.py'])