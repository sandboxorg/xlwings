import xlwings as xw

wb = xw.Workbook()

xw.Range("A1").value = 3

print(xw.Range("A1").value)