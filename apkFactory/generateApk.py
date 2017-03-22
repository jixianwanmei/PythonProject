# encoding: utf-8
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

def generateApk(idStr,nameStr):
	# os.chdir('/Users/lidongsheng/Desktop/apkFactory')
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
		f2.write(s.replace('1319138',idStr).replace('bdgw01shz_apk',nameStr))

	f1.close()
	f2.close()
	os.remove('shz_Config.json')
	os.rename('shz_Config2.json','shz_Config.json')


	print '------------------------------------2 : change configs finished'
	os.chdir('../../../')
	#update the app icon
	#enter iconfile
	os.chdir('icons/'+nameStr)	
	if os.path.exists('baseIcon.png'):
		# if the generated icon was exists then pass
		if not os.path.exists('baseIcon'):
			os.system('icontool baseIcon.png')
		# remove the older png hdpi
		if os.path.exists('../../ShuiHuZhuanPhone-release-signed/res/drawable-hdpi-v4/icon.png'):
			os.remove('../../ShuiHuZhuanPhone-release-signed/res/drawable-hdpi-v4/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-hdpi/icon.png','../../ShuiHuZhuanPhone-release-signed/res/drawable-hdpi-v4/')

		# remove the older png ldpi
		if os.path.exists('../../ShuiHuZhuanPhone-release-signed/res/drawable-ldpi-v4/icon.png'):
			os.remove('../../ShuiHuZhuanPhone-release-signed/res/drawable-ldpi-v4/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-ldpi/icon.png','../../ShuiHuZhuanPhone-release-signed/res/drawable-ldpi-v4/')

		# remove the older png mdpi
		if os.path.exists('../../ShuiHuZhuanPhone-release-signed/res/drawable-mdpi-v4/icon.png'):
			os.remove('../../ShuiHuZhuanPhone-release-signed/res/drawable-mdpi-v4/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-mdpi/icon.png','../../ShuiHuZhuanPhone-release-signed/res/drawable-mdpi-v4/')

		# remove the older png xhdpi
		if os.path.exists('../../ShuiHuZhuanPhone-release-signed/res/drawable-xhdpi-v4/icon.png'):
			os.remove('../../ShuiHuZhuanPhone-release-signed/res/drawable-xhdpi-v4/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-xhdpi/icon.png','../../ShuiHuZhuanPhone-release-signed/res/drawable-xhdpi-v4/')

		# remove the older png xxhdpi
		if os.path.exists('../../ShuiHuZhuanPhone-release-signed/res/drawable-xxhdpi-v4/icon.png'):
			os.remove('../../ShuiHuZhuanPhone-release-signed/res/drawable-xxhdpi-v4/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-xxhdpi/icon.png','../../ShuiHuZhuanPhone-release-signed/res/drawable-xxhdpi-v4/')
		
	#改app名字 
	# newAppName = '百易水浒传'	
	# os.chdir('../../ShuiHuZhuanPhone-release-signed/res/values/')
	# f1 = open('strings.xml')
	# f2 = open('strings2.xml','w')
	# for s in f1.readlines():
	# 	f2.write(s.replace('街机水浒传',str(newAppName)))
	# f1.close()
	# f2.close()
	# os.remove('strings.xml')
	# os.rename('strings2.xml','strings.xml')
	# os.chdir('../')

	# re zip the apk
	os.chdir('../../')
	os.system('apktool b ShuiHuZhuanPhone-release-signed')
	print '------------------------------------3 : re zip apk '
	print('# enter dist to resign apk')
	os.chdir('ShuiHuZhuanPhone-release-signed/dist/')

	reSignStr = 'jarsigner -verbose -keystore ../../baiyikeji-baidu-google.keystore -storepass 123456 -signedjar '+nameStr+'.apk -digestalg SHA1 -sigalg MD5withRSA ShuiHuZhuanPhone-release-signed.apk baiyikeji.keystore '
	os.system(reSignStr)
	print '------------------------------------4 : resign apk '
	if os.path.exists('../../product/'+nameStr+'.apk'):
		os.remove('../../product/'+nameStr+'.apk')
	if not os.path.exists('../../product/'):
		os.makedirs('../../product/')

	shutil.move(nameStr+'.apk','../../product/')
	os.chdir('../../')
	shutil.rmtree('ShuiHuZhuanPhone-release-signed')
	print(nameStr,'one apk was finished')

# for i in range(len(channelArray)):
# 	fIdStr = channelArray[i][0]
# 	fNameStr = channelArray[i][1]
# 	generateApk(fIdStr,fNameStr)
# 	print '------------------------------------------------------------',str(i+1)+'/'+str(len(channelArray))


#当乐
# generateApk('1008832','dlshz_apk')


# #官网fx
# generateApk('1000063','gwfxshz_apk')
# #吴钰钰推广渠道；
# generateApk('1113838','wuyuyu_apk')

# #  pc6
# generateApk('1056962','PC6CPSshz_apk')
# # #玩游戏网
# generateApk('1546801','wyxCPS_apk')
# # #优亿
# generateApk('1148873','yyscCPS_apk')

# #官网
# generateApk('1000058','gwshz_apk')
# #百度竞价
# generateApk('1003689','bdgw01shz_apk')
# #新分享渠道
# generateApk('1005709','nfxshz_apk')
# #新推广渠道
# generateApk('1319134','shz_NTG_apk')

# 优盟易 12345
generateApk('1238269','youmengyicps1')
generateApk('1238271','youmengyicps2')
generateApk('1238273','youmengyicps3')
generateApk('1238277','youmengyicps4')
generateApk('1238279','youmengyicps5')

   


 
 

