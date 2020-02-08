import os, openpyxl
os.chdir('C:\\Users\\jackk\\Documents\\Python Things\\Spreadsheets\\')

workbook = openpyxl.load_workbook('example.xlsx')
print(workbook.sheetnames)
worksheet = workbook['Sheet1']
print(str(worksheet['a1'].value))
print(worksheet['b1'].value)
print(worksheet.cell(row = 1, column = 2).value)
print('\n')
for i in range(1,8):
    print(i,worksheet.cell(row = i, column = 2).value)


