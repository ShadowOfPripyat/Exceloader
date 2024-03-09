# Exceloader
My way to load excel files from panda, and call the things i want. It's basically like a library.

# Usage:
### To load an excel file:

```python
from exceloader import ExcelReader

excel_reader = ExcelReader(C:\\User\\Documents\\file.xlsx)
```

### To get the number of worksheets that the file contains:
```python
print(num_worksheets)
```

### Get original worksheet name (May not work gud neither)
```python
original_sheet_names = excel_reader.get_original_sheet_names()
print("Original sheet names:", original_sheet_names)
```

### Read a specific worksheet (May not work gud neither)
```python
sheet_name = 'Sheet1'
wsh1 = excel_reader.read_worksheet(sheet_name)
print(f"\nData from '{sheet_name}':")
print(wsh1)
```
