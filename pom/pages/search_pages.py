import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class search_Page:
    def __init__(self, driver):
        self.driver = driver
        self.btn_search = (
            # By.CSS_SELECTOR, ".AppHeader-searchButton.form-control.text-left.color-fg-subtle.no-wrap.placeholder")
            By.CSS_SELECTOR, "body > div.logged-in.env-production.page-responsive >"
                             " div.position-relative.header-wrapper.js-header-wrapper "
                             "> header > div > div.AppHeader-globalBar-end > div.AppHeader-search >"
                             " qbsearch-input > div.search-input-container.search-with-dialog.position"
                             "-relative.d-flex.flex-row.flex-items-center.height-auto.color-bg-transparent."
                             "border-0.color-fg-subtle.mx-0 > div.AppHeader-search-whenRegular > div > div > button" )
        self.into_SearchBox = (By.CSS_SELECTOR, "#query-builder-test")

        self.body = (By.TAG_NAME, "body")

    def searchRepository(self, repoName):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.btn_search)
        ).click()
        # Chờ search box xuất hiện và có thể nhập
        search_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.into_SearchBox)
        )
        time.sleep(1)
        search_box.clear()
        search_box.send_keys(repoName)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)



