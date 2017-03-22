import os,shutil
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
channelArray = []
data = xlrd.open_workbook('channels.xlsx')
sheet1 = data.sheets()[0]
num_rows = sheet1.nrows
num_cols = sheet1.ncols
for rowNum in range(num_rows):
	typeCell = sheet1.cell_value(rowNum,8)
	platformCell = sheet1.cell_value(rowNum,9)
	if (str(typeCell)=='CPS' and str(platformCell)=='Adroid'):
		idCell = sheet1.cell_value(rowNum,0)
		nameCell = sheet1.cell_value(rowNum,7)
		idStr = str(int(idCell))
		nameStr = str(nameCell)
		arr = []
		arr.append(idStr)
		arr.append(nameStr)
		channelArray.append(arr)

os.chdir('icons')
for i in range(len(channelArray)):
	iconPath = channelArray[i][1]
	if not (os.path.isdir(iconPath)):
		os.makedirs(iconPath)
