import time
from pathlib import Path
import pytest
from pom.pages.repository_pages import repository_pages
from pom.pages.file_Reader import FileReaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# lấy đường dãn file input và output
dataPath = Path(__file__).parent.parent / "Data" / "Data_Excel_test_delete.xlsx"
OUTPUT_Path = Path(__file__).parent.parent / "Result" / "Result_Xlsx_test_delete.xlsx"
# tạo đối tượng đọc
reader = FileReaderPage(dataPath)
# đọc file input
df = reader.read_excel()
# thêm vào cột Result để lưu vào vị trí file output
if "Result" not in df.columns:
    df["Result"] = ""
# Lấy index để biết dòng nào khi ghi kết quả
test_data = list(df[["Name", "Link"]].itertuples(index=True, name=None))

@pytest.mark.parametrize("idx, Name, Link", test_data)
def test_deleteRepositori(driver, idx, Name, Link):
    repository_page = repository_pages(driver)
    name = Name
    # đường dẫn tới trang settingss
    link = Link
    # mở rang settings
    repository_page.open(link)
    result = ''
    time.sleep(1)
    try:
        # thực hiện chức năng xóa Repo
        repository_page.deleteRepo(name)
        # sau đây là cấu hình để nhận thanh thông báo chứa "was successfully deleted"
        alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.js-flash-alert")))
        alert_text = alert.text
        # cắt đoạn đó ra
        repo_name = alert_text.split('"')[1]
        # kiểm tra nếu xuất thông báo đã xóa
        assert "was successfully deleted" in alert_text
        # và repo có trong thông báo trùng với name cần xóa thì pass
        assert repo_name == name
        result = "PASS"
    except Exception:
        result = "FAIL"
        raise
    finally:# lưu file kết quả
        df.loc[idx,"Result"] = result
        reader.write_excel(df, OUTPUT_Path)
