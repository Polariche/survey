import openpyxl

wb = Workbook()
ws = wb.active

data = [['asdf','asdf','asdf'], ['asdas', 'asdff', 'asdffasd']]

for row in data:
    ws.append(row)

wb.save('example1.xlsx')
print(type(wb))

