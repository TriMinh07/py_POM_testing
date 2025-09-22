import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Home_pages:
    def __init__(self, driver):
        # nhận driver
        self.driver = driver
        # nút mở menu tùy chọn thêm mới
        self.btn_MenuAddRepository = (By.ID,"global-create-menu-anchor")
        # nút chọn thêm mới Repository
        self.addRepository = (By.XPATH, "//a[@href='/new']")
        # ô nhập tên Repository
        self.repositoryName = (By.ID, "repository-name-input")
        # ô nhập mô tả của Repository
        self.repositoryDescription = (By.NAME, "Description")
        # nút xác nhận thêm mới
        self.btn_CreateRepository = (By.XPATH, "/html/body/div[1]/div[6]/main/react-app/div/form/div[4]/button")

    def addNewRepository(self, Repo_Name, Repo_Desc):
        #click nút mở menu tùy chọn thêm mới
        self.driver.find_element(*self.btn_MenuAddRepository).click()
        #click nút chọn thêm mới Repository
        self.driver.find_element(*self.addRepository).click()
        #nhập liệu ô nhập tên Repository

        # 2. Chờ trường input xuất hiện mới thao tác
        repositoryName = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.repositoryName)
        )
        repositoryName.click()
        repositoryName.clear()
        repositoryName.send_keys(Keys.CONTROL + "a")  # chọn toàn bộ text
        repositoryName.send_keys(Keys.DELETE)  # xóa sạch
        repositoryName.send_keys(Repo_Name)

        #nhập liệu ô nhập mô tả của Repository
        Description = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.repositoryDescription)
        )
        Description.clear()
        Description.send_keys(Repo_Desc)
        # chờ để hệ thống xác nhận tên  hợp lệ
        time.sleep(3)
        # lấy nút xác nhận thêm mới
        create_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.btn_CreateRepository)
        )
        # Scroll xuống cuối trang
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # click thêm mới
        create_button.click()



