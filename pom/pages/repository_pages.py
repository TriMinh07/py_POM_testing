import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class repository_pages:
    def __init__(self, driver):
        self.driver = driver
        # lấy nút xóa trong trang cài đặt
        self.btn_Delete = (By.CSS_SELECTOR, ".js-repo-delete-button.Button--danger")
        # nút confirm đầu tiên
        self.btn_I_WannaDelete = (By.CSS_SELECTOR, ".js-repo-delete-proceed-button.Button--secondary")
        # nút đọc điều khoảng và chấp nhận xóa
        self.btn_I_AcceptDeleteWarning = (By.ID, "repo-delete-proceed-button")
        # ô nhập liệu: nhập tên repo để xóa
        self.name_to_delete = (By.CSS_SELECTOR, ".js-repo-delete-proceed-confirmation")
        # nút xóa hiện ra sau khi nhập liệu xong
        self.btn_Delete_Last = (By.ID, "repo-delete-proceed-button")
        #xác thực email. có thể có hoặc không
        self.btn_confirm = (By.ID, "sudo-send-email")
        # sau khi nhập xác thực email sẽ có nút verify hiện ra
        self.btn_verify = (By.CSS_SELECTOR, ".Button--primary.Button--medium.Button--fullWidth")


    def open(self, url):
        # hàm này dùng để mở link đến settings của repo
        self.driver.get(url)

    def deleteRepo(self, link):
        # Kéo xuống cuối trang (nút Delete nằm cuối)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Click Delete button
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.btn_Delete)
        ).click()
        time.sleep(1)

        # Confirm delete lần 1
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.btn_I_WannaDelete)
        ).click()
        time.sleep(1)

        # Ấn nút "I have read and understand these effects" - lần 2
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_I_AcceptDeleteWarning)
        ).click()
        time.sleep(1)

        # Nhập tên repo để xác nhận
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.name_to_delete)
        ).send_keys(link)
        time.sleep(1)

        # Click nút Delete cuối
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_Delete_Last)
        ).click()
        time.sleep(1)

        # Nếu có bước xác nhận email
        try:
            self.driver.find_element(*self.btn_confirm).click()
        except:
            print("Không cần confirm email")
