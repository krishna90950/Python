import xlrd
from itertools import islice

import pandas as pd

path = r"C:\Users\Krishna\Desktop\Python course learning\Selpy1.xls"

workbook_obj = xlrd.open_workbook(path)
print(workbook_obj)

worksheet_obj = workbook_obj.sheet_by_name("data")
print(worksheet_obj)
rows = worksheet_obj.get_rows()

# for row in rows:
#     print(row[0].value, row[1].value)
# rows = worksheet_obj.get_rows()
header = next(rows)
# print(header)
d = {row[0].value: row[1].value for row in rows}
# print(d)
# d = {}
# for row in rows:
#     d[row[0].value] = row[1].value
# print(d)

# d = {}
# first_iteration = True
# for row in rows:
#     if first_iteration:
#         first_iteration = False
#         continue
#     d[row[0].value] = row[1].value
# print(d)

# d = {}
# for row in rows:
#     d[row[0].value] = row[1].value
# print(d)
