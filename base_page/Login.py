from pageObject.login_page import LoginPage

def start_login_success(phone,password):

    lg = LoginPage('http://ymhtml.lecoding.cn/#/home/login', 'firefox')
    lg.driver.maximize_window()
    lg.input_username(phone)
    lg.input_pwd(password)
    lg.login_button()
    lg.driver.implicitly_wait(30)


