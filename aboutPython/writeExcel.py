 #coding=utf-8
import xlwt 
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
for i in range(40):
	for j in range(40):
		sheet1.write(i,j,'('+str(i)+','+str(j)+')')

workbook.save('pyWrite.xls')
print 'finish excel'