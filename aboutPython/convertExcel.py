#coding=utf-8
import xlwt 
import xlrd
oldXls = raw_input('Enter a xls name :')
workbook = xlwt.Workbook()
wSheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
print type(oldXls)
data = xlrd.open_workbook(str(oldXls))
sheet1 = data.sheets()[0]
num_rows = sheet1.nrows
num_cols = sheet1.ncols
for row in range(num_rows):
	for col in range(num_cols):
		cell = sheet1.cell_value(row,col)
		wSheet1.write(col,row,cell)
workbook.save('converted.xls')