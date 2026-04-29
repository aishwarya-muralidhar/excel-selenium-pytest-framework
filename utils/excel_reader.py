import pandas as pd

def read_excel_file(file_path, sheet_name = 0):
    """
    Reads Excel file and returns DataFrame
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
