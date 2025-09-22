import pytest
import pandas as pd
from pathlib import Path
from pom.pages import login_pages
from pom.pages.file_Reader import FileReaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# lấy đường dãn file input và output
dataPath = Path(__file__).parent.parent / "Data" / "Data_Excel_test_login_e2e.xlsx"
OUTPUT_Path = Path(__file__).parent.parent / "Result" / "Result_Xlsx_test_login.xlsx"
# tạo đối tượng đọc
reader = FileReaderPage(dataPath)
# đọc file input
df = reader.read_excel()
# thêm vào cột Result để lưu vào vị trí file output
if "Result" not in df.columns:
    df["Result"] = ""

# Lấy dữ liệu test (username, password, Expected)
test_data = df[["username", "password", "Expected"]].values.tolist()

@pytest.mark.parametrize("username,password,Expected", test_data)
def test_login_success(driver, username, password, Expected):
    login_page = login_pages.LoginPage(driver)
    # mở trang Github
    login_page.open("https://github.com/login")
    # tạo biến để lưu tạm kết quả
    result = ''
    try:
        # thực hiện CN đăng nhập
        login_page.login(username, password)
        # lấy avata của trang web sau đnawg nhập để kiểm tra
        avatar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Expected))
        )
        # nếu avata trùng với Expected thì test case pass
        assert avatar is not None
        result = "PASS"
    except Exception:
        # bắt ngoại lệ trường hợp fail
        result = "FAIL"
        raise   # để pytest vẫn báo fail
    finally:
        # //cuối cùng, lấy vị trí Result của test case đang test
        idx = test_data.index([username, password, Expected])
        # Result được lưu
        df.loc[idx, "Result"] = result
        # gọi hàm lưu file excel
        reader.write_excel(df, OUTPUT_Path)