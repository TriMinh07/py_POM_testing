from selenium.webdriver.common.by import By

class LoginPage:
    #chạy khi bắt đầu
    def __init__(self, driver):
        #driver chạy test
        self.driver = driver
        self.username_input = (By.NAME, "login")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.NAME, "commit")

    #lấy UlR
    def open(self, url):
        self.driver.get(url)

    #hàm đăng nhập
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
