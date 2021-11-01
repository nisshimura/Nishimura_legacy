import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.title = 'TEST'

ws['A1'] = '西村喬行'
    
wb.save('pyinst_test.xlsx')
