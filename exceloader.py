import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.xls = pd.ExcelFile(file_path)
            self.sheet_names = self.xls.sheet_names
        except Exception as e:
            raise ValueError(f"Error opening Excel file: {e}")

    def count_worksheets(self):
        return len(self.sheet_names)

    def get_original_sheet_names(self):
        return self.sheet_names

    def read_worksheet(self, sheet_name):
        try:
            return pd.read_excel(self.xls, sheet_name)
        except Exception as e:
            raise ValueError(f"Error reading worksheet '{sheet_name}': {e}")

    def set_file_path(self, file_path):
        self.file_path = file_path
        try:
            self.xls = pd.ExcelFile(file_path)
            self.sheet_names = self.xls.sheet_names
        except Exception as e:
            raise ValueError(f"Error opening Excel file: {e}")
