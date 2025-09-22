import time
from pathlib import Path

import pytest

from pom.pages import search_pages
from pom.pages.file_Reader import FileReaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# lấy đường dãn file input và output
dataPath = Path(__file__).parent.parent / "Data" / "Data_Excel_test_search.xlsx"
OUTPUT_Path = Path(__file__).parent.parent / "Result" / "Result_Xlsx_test_search.xlsx"
# tạo đối tượng đọc
reader = FileReaderPage(dataPath)
# đọc file input
df = reader.read_excel()
# thêm vào cột Result để lưu vào vị trí file output
if "Result" not in df.columns:
    df["Result"] = ""

# lấy dữ liệu, tạo index
test_data = df[["SearchName", "Expected"]].itertuples(index=True, name=None)

@pytest.mark.parametrize("idx, SearchName, Expected ", test_data)
def test_Search_Repo(driver, idx, SearchName, Expected):
    searchPage = search_pages.search_Page(driver)
    # lấy tên repo cần search
    repoName = SearchName
    # tạo biến để lưu tạm kết quả
    result = ""
    try:
        #cho hệ thống chờ tránh xẩy ra lỗi
        time.sleep(2)
        # thực hiện CN tìm kiếm Repository
        searchPage.searchRepository(repoName)
        # href này là vị trí repo cần tiềm
        href = f"//a[@href='/{Expected}']"
        # tìm kiếm kết quả
        link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, href))
        )
        # nếu có đường link cần tìm thì pass
        assert link is not None
        result = "PASS"
    except Exception:
        result = "FAIL"
        raise
    finally:
        # thêm vào biến dữ liệu
        df.loc[idx,"Result"] = result
        # lưu file kết quả
        (reader.write_excel(df, OUTPUT_Path))


