import time
import pytest
from pom.pages import home_pages
from pom.pages.file_Reader import FileReaderPage
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# lấy đường dãn file input và output
dataPath = Path(__file__).parent.parent / "Data" / "Data_Excel_test_creNewRepo.xlsx"
OUTPUT_Path = Path(__file__).parent.parent / "Result" / "Result_Xlsx_test_creNewRepo.xlsx"
# tạo đối tượng đọc
reader = FileReaderPage(dataPath)
# đọc file input
df = reader.read_excel()
# thêm vào cột Result để lưu vào vị trí file output
if "Result" not in df.columns:
    df["Result"] = ""
# Lấy index để biết dòng nào khi ghi kết quả
test_data = list(df[["RepoName", "RepoDesc", "Expected"]].itertuples(index=True, name=None))

@pytest.mark.parametrize("idx,RepoName,RepoDesc,Expected", test_data)
def test_createNewRepo(driver, idx, RepoName, RepoDesc, Expected):
    # nhận driver
    home_page = home_pages.Home_pages(driver)
    # nhận input nameRepo và Desc
    nameRepo = RepoName
    descRepo = RepoDesc
    # nhận Expected
    xPath = Expected
    result = ''
    try:
        # thực hiện chức năng tạo Repo
        home_page.addNewRepository(nameRepo, descRepo)
        # lấy link để kiểm tra
        link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )
        # nếu link có tồn tại = Expected trong trang thì sẽ pass
        assert link is not None
        result = "PASS"
    except Exception: #ngược lại sẽ fail
        result = "FAIL"
        raise
    finally:
        # vì đã có index trước nên ta không cần tìm lại
        df.loc[idx, "Result"] = result
        # lưu file kết quả
        reader.write_excel(df, OUTPUT_Path)
