import os,shutil
import xlrd
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')
# channelArray = []
# data = xlrd.open_workbook('channels.xlsx')
# sheet1 = data.sheets()[0]
# num_rows = sheet1.nrows
# num_cols = sheet1.ncols
# for rowNum in range(num_rows):
# 	idCell = sheet1.cell_value(rowNum,0)
# 	nameCell = sheet1.cell_value(rowNum,7)
# 	idStr = str(idCell)
# 	nameStr = str(nameCell)
# 	arr = []
# 	arr.append(idStr)
# 	arr.append(nameStr)
# 	channelArray.append(arr)

os.chdir('/Users/lidongsheng/Desktop/apkFactory')

if (os.path.isdir('ShuiHuZhuanPhone-release-signed')):
	shutil.rmtree('ShuiHuZhuanPhone-release-signed')
	print '------------------------------------0 if ShuiHuZhuanPhone-release-signed exists then remove it '

os.system('apktool d ShuiHuZhuanPhone-release-signed.apk')
print '------------------------------------1 : unzip apk'
print('# enter assets res dir')
os.chdir('ShuiHuZhuanPhone-release-signed/assets/res/')
f1 = open('shz_Config.json')
f2 = open('shz_Config2.json','w')
for s in f1.readlines():
	f2.write(s.replace('1319138','12345678').replace('bdgw01shz_apk','new_cps_apk'))

f1.close()
f2.close()
os.remove('shz_Config.json')
os.rename('shz_Config2.json','shz_Config.json')
print '------------------------------------2 : change configs finished'
os.chdir('../../../')
os.system('ls')
os.system('apktool b ShuiHuZhuanPhone-release-signed')
print '------------------------------------3 : re zip apk '
print('# enter dist to resign apk')
os.chdir('ShuiHuZhuanPhone-release-signed/dist/')

reSignStr = 'jarsigner -verbose -keystore ../../baiyikeji-baidu-google.keystore -storepass 123456 -signedjar new_cps.apk -digestalg SHA1 -sigalg MD5withRSA ShuiHuZhuanPhone-release-signed.apk baiyikeji.keystore '
os.system(reSignStr)
print '------------------------------------4 : resign apk '
shutil.move('new_cps.apk','../../product/')
os.chdir('../../')
shutil.rmtree('ShuiHuZhuanPhone-release-signed')
print('one apk was finished')

