import pytest
from selenium import webdriver
from pom.pages import login_pages
@pytest.fixture(scope="session") #khởi tạo fixture 1 lần duy nhất
def driver():
    # mở trình duyệt
    driver = webdriver.Chrome()
    # phóng to cửa sổ
    driver.maximize_window()
    # trả về driver cho test sử dụng
    yield driver
    # sau khi chạy test xong đóng driver
    driver.quit()
#hàm dùng để lưu session đăng nhập giúp không phải đăng nhập ở mỗi test
@pytest.fixture(scope="session")
def logged_in_driver(driver):
    # nhận driver từ fixture driver
    # nhận đối tương login page
    login_page = login_pages.LoginPage(driver)
    # mở trang Github
    login_page.open("https://github.com/login")
    # thực hiện login
    login_page.login("baitap472004", "Lambai1234@")
    # trả về driver đã đăng nhập
    return driver

