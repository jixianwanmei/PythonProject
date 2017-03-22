#coding=utf-8
#把excel里面的文本自动化成lua里面的变量名
import os 
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
ls = os.linesep
excelPath = 'sgjMusic.xlsx'
data = xlrd.open_workbook(excelPath)
sheet1 = data.sheets()[5]
num_rows = sheet1.nrows
num_cols = sheet1.ncols
all = []
for row in range(num_rows):
	if row !=0:
		print type(sheet1.cell_value(row,1))
		cell1 = sheet1.cell_value(row,1)
		cell1Str = cell1.encode("utf-8")

		str1 = '--'+cell1Str
		all.append(str1)
		cell3 = sheet1.cell_value(row,3) 
		cell3Str = cell3.encode("utf-8")
		cell3Arr = cell3Str.rsplit('.')
		str2 = 'SGJMusicMusicConfig.'+cell3Arr[0]+' = "Games/SGJ/Source/audio/'+cell3Arr[0]+'"'
		all.append(str2)

fobj = open('audio.lua','w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'completed'