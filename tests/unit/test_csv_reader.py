import pytest
import pandas as pd
from pathlib import Path
from pom.pages.file_Reader import FileReaderPage
from src.calculator import do_Operation

# Đường dẫn tới file CSV
CSV_Path = Path(__file__).parent.parent / "Data" / "Data_CSV_test_calculator.csv"
OUTPUT_Path = Path(__file__).parent.parent / "Result" / "Result_CSV_test.csv"

# Đọc dữ liệu 1 lần duy nhất
reader = FileReaderPage(CSV_Path)
df = reader.read_csv()

# Nếu chưa có cột Result thì thêm vào
if "Result" not in df.columns:
    df["Result"] = ""

if "Actual" not in df.columns:
    df["Actual"] = ""

# Chuyển DataFrame thành list of tuples [(a, b, operation, expected), ...]
test_data = df[["a", "b", "operation", "expected"]].values.tolist()
def test_Read_CSV():
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_File_Not_found_CSV():
    reader = FileReaderPage("wrong_path.csv")
    with pytest.raises(ValueError):
        reader.read_csv()

# Parametrize để chạy từng dòng dữ liệu
@pytest.mark.parametrize("idx,a,b,operation,expected", [(i, *row) for i, row in enumerate(test_data)])
def test_Calculator(idx, a, b, operation, expected):
    try:
        if str(expected).lower() in ["zerodivisionerror", "divide by zero"]:
            # Trường hợp mong đợi là chia cho 0
            with pytest.raises(ZeroDivisionError):
                do_Operation(float(a), float(b), operation)
            df.at[idx, "Actual"] = "ZeroDivisionError"
            df.at[idx, "Result"] = "PASS"

        else:
            # Trường hợp mong đợi là một giá trị số
            Output = do_Operation(float(a), float(b), operation)
            assert Output == float(expected)
            df.at[idx, "Actual"] = round(Output, 2)
            df.at[idx, "Result"] = "PASS"

    except AssertionError:
        df.at[idx, "Result"] = "FAIL"
        raise
    except Exception as e:
        df.at[idx, "Result"] = f"FAIL - {type(e).__name__}"
        raise

def teardown_module(module):
    #Sau khi chạy hết test, lưu kết quả vào file result
    OUTPUT_Path.parent.mkdir(parents=True, exist_ok=True)  # tạo folder nếu chưa có
    df.to_csv(OUTPUT_Path, index=False)

def test_result_file_saved():
    #Kiểm tra file kết quả đã được lưu thành công
    assert OUTPUT_Path.exists(), "File kết quả chưa tồn tại"
    assert OUTPUT_Path.stat().st_size > 0, "File kết quả rỗng"

    result_df = pd.read_csv(OUTPUT_Path)
    assert not result_df.empty, "Dữ liệu trong file kết quả rỗng"
