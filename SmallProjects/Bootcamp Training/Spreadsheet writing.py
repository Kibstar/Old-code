import os, openpyxl

os.chdir(r'C:\Users\jackk\Documents\Python Things\Spreadsheets')
wb = openpyxl.Workbook()
print(wb.sheetnames)
sheet = wb['Sheet']

print(sheet['a1'].value)
sheet['a1'] = 42
sheet['b2'] = 42
print(sheet['a1'].value)
wb.save('Excel writing example.xlsx')

wb.create_sheet('Sheet two')
sheet2 = wb['Sheet two']

wb.create_sheet(index = 0,title = 'My New Sheet')
print(wb.sheetnames)
wb.save('Excel writing example.xlsx')