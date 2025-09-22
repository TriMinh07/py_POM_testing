import pandas as pd
from pathlib import Path

class FileReaderPage:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        try:
            df = pd.read_csv(self.file_path)  # luôn trả về DataFrame
            return df
        except Exception as e:
            raise ValueError(f"Lỗi đọc CSV: {e}")

    def read_excel(self) -> pd.DataFrame:
        try:
            df = pd.read_excel(self.file_path, engine="openpyxl")
            return df
        except Exception as e:
            raise ValueError(f"Lỗi khi đọc Excel: {e}")

    def write_excel(self, df, save_path=None):
        if save_path is None:
            save_path = self.filepath
        else:
            save_path = Path(save_path)

        with pd.ExcelWriter(save_path, engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, index=False)