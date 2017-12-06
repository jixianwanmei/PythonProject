# encoding: utf-8
import os,shutil
import xlrd
import sys
reload(sys)

#1改配置
#2改icon
#3改应用名（如果需要）
#4改包名（如果需要）
def generateApk(idStr,nameStr,appName,pkgName):
	#改配置 渠道号什么的；
	os.chdir('../../ShuiHuZhuan/res/')
	f1 = open('shz_Config.json')
	f2 = open('shz_Config2.json','w')
	for s in f1.readlines():
		f2.write(s.replace('1319138',idStr).replace('bdgw01shz_apk',nameStr))

	f1.close()
	f2.close()
	os.remove('shz_Config.json')
	os.rename('shz_Config2.json','shz_Config.json')
	print '-------------------------change configs finished 1'

	os.chdir('../../PythonProject/apkFactory/icons/'+nameStr)
	#改icon
	if os.path.exists('baseIcon.png'):
		# if the generated icon was exists then pass
		if not os.path.exists('baseIcon'):
			os.system('icontool baseIcon.png')
		iconPathRoot = '../../../../ShuiHuZhuan/frameworks/runtime-src/proj.android/res/'
		# remove the older png hdpi
		if os.path.exists(iconPathRoot + 'drawable-hdpi/icon.png'):
			os.remove(iconPathRoot + 'drawable-hdpi/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-hdpi/icon.png',iconPathRoot + 'drawable-hdpi/')

		# remove the older png ldpi
		if os.path.exists(iconPathRoot + 'drawable-ldpi/icon.png'):
			os.remove(iconPathRoot + 'drawable-ldpi/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-ldpi/icon.png',iconPathRoot + 'drawable-ldpi/')

		# remove the older png mdpi
		if os.path.exists(iconPathRoot + 'drawable-mdpi/icon.png'):
			os.remove(iconPathRoot + 'drawable-mdpi/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-mdpi/icon.png',iconPathRoot + 'drawable-mdpi/')

		# remove the older png xhdpi
		if os.path.exists(iconPathRoot + 'drawable-xhdpi/icon.png'):
			os.remove(iconPathRoot + 'drawable-xhdpi/icon.png')
		# move the generated icon to the app zip file 
		shutil.copy('baseIcon/drawable-xhdpi/icon.png',iconPathRoot + 'drawable-xhdpi/')

		# # remove the older png xxhdpi
		# if os.path.exists(iconPathRoot + 'drawable-xxhdpi/icon.png'):
		# 	os.remove(iconPathRoot + 'drawable-xxhdpi/icon.png')
		# # move the generated icon to the app zip file 
		# shutil.copy('baseIcon/drawable-xxhdpi/icon.png',iconPathRoot + 'drawable-xxhdpi/')
		os.chdir('../../../../ShuiHuZhuan/')

	#改应用名
	if (appName != '街机水浒传'):
		os.chdir('frameworks/runtime-src/proj.android/res/values/')
		f1 = open('strings.xml')
		f2 = open('strings2.xml','w')
		for s in f1.readlines():
			f2.write(s.replace('街机水浒传',appName))
		f1.close()
		f2.close()
		os.remove('strings.xml')
		os.rename('strings2.xml','strings.xml')
		os.chdir('../../../../../')
	#改包名
	if (pkgName!='com.baiyikeji.jiejishuihuzhuan'):
		os.chdir('frameworks/runtime-src/proj.android/src/com/baiyikeji/jiejishuihuzhuan/wxapi')

		f1 = open('WXPayEntryActivity.java')
		f2 = open('WXPayEntryActivity2.java','w')
		for s in f1.readlines():
			f2.write(s.replace('com.baiyikeji.jiejishuihuzhuan.R',pkgName+'.R'))
		f1.close()
		f2.close()
		os.remove('WXPayEntryActivity.java')
		os.rename('WXPayEntryActivity2.java','WXPayEntryActivity.java')
		os.chdir('../../../by/shz/util/')

		file1 = open('FileDownLoadUtil.java')
		file2 = open('FileDownLoadUtil2.java','w')
		for s in file1.readlines():
			file2.write(s.replace('com.baiyikeji.jiejishuihuzhuan.R',pkgName+'.R'))
		file1.close()
		file2.close()
		os.remove('FileDownLoadUtil.java')
		os.rename('FileDownLoadUtil2.java','FileDownLoadUtil.java')

		os.chdir('../../../../../')
		
		mainfest1 = open('AndroidManifest.xml')
		mainfest2 = open('AndroidManifest2.xml','w')
		for s in mainfest1.readlines():
			mainfest2.write(s.replace('package=\"com.baiyikeji.jiejishuihuzhuan\"','package=\"'+pkgName+'\"'))
		mainfest1.close()
		mainfest2.close()
		os.remove('AndroidManifest.xml')
		os.rename('AndroidManifest2.xml','AndroidManifest.xml')
		os.chdir('../../../')
	

	
	print('打印一下当前路径1')
	print os.getcwd()

	os.system('cocos compile -p android -m release ')
	#编译完以后把名字改成 对应的apk名字
	print('打印一下当前路径2')
	os.chdir('publish/android')
	print os.getcwd()
	os.rename('ShuiHuZhuanPhone-release-signed.apk',nameStr+'.apk')
	os.chdir('../../')
	
	#改回应用名
	if (appName != '街机水浒传'):
		os.chdir('frameworks/runtime-src/proj.android/res/values/')
		f1 = open('strings.xml')
		f2 = open('strings2.xml','w')
		for s in f1.readlines():
			f2.write(s.replace(appName,'街机水浒传'))
		f1.close()
		f2.close()
		os.remove('strings.xml')
		os.rename('strings2.xml','strings.xml')
		os.chdir('../../../../../')

	#改回包名
	if (pkgName!='com.baiyikeji.jiejishuihuzhuan'):
		os.chdir('frameworks/runtime-src/proj.android/src/com/baiyikeji/jiejishuihuzhuan/wxapi')

		f1 = open('WXPayEntryActivity.java')
		f2 = open('WXPayEntryActivity2.java','w')
		for s in f1.readlines():
			f2.write(s.replace(pkgName+'.R','com.baiyikeji.jiejishuihuzhuan.R'))
		f1.close()
		f2.close()
		os.remove('WXPayEntryActivity.java')
		os.rename('WXPayEntryActivity2.java','WXPayEntryActivity.java')
		os.chdir('../../../by/shz/util/')

		file1 = open('FileDownLoadUtil.java')
		file2 = open('FileDownLoadUtil2.java','w')
		for s in file1.readlines():
			file2.write(s.replace(pkgName+'.R','com.baiyikeji.jiejishuihuzhuan.R'))
		file1.close()
		file2.close()
		os.remove('FileDownLoadUtil.java')
		os.rename('FileDownLoadUtil2.java','FileDownLoadUtil.java')

		os.chdir('../../../../../')
		
		mainfest1 = open('AndroidManifest.xml')
		mainfest2 = open('AndroidManifest2.xml','w')
		for s in mainfest1.readlines():
			mainfest2.write(s.replace(pkgName,'com.baiyikeji.jiejishuihuzhuan'))
		mainfest1.close()
		mainfest2.close()
		os.remove('AndroidManifest.xml')
		os.rename('AndroidManifest2.xml','AndroidManifest.xml')
		os.chdir('../../../')
	


	#把改过的配置改回去 以便于下次修改
	os.chdir('SHZRes/config')
	f1 = open('shz_Config.json')
	f2 = open('shz_Config2.json','w')
	for s in f1.readlines():
		f2.write(s.replace(idStr,'1319138').replace(nameStr,'bdgw01shz_apk'))
	f1.close()
	f2.close()
	os.remove('shz_Config.json')
	os.rename('shz_Config2.json','shz_Config.json')

	os.chdir('../../PythonProject/apkFactory')
 
# generateApk('1464435','shzlhj_apk','老虎机水浒传','com.shengqukeji.shuihuzhuan')
# generateApk('1568414','hfrn_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')



 #逸游无线
# generateApk('1517607','YY0902SHZ_akp','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1517608','YY0903SHZ_akp','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
  
#近游 深圳新接
# 渠道ID：1578810 
# 渠道账号： jy_cps_apk 
# generateApk('1578810','jy_cps_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')


#八月十八
# generateApk('1509065','shzyt818_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')


#   1238280 youmengyicps6 优盟易cps6 
# 1238283 youmengyicps7 优盟易7 
# 1238285 youmengyicps8 优盟易8 
# 1238288 youmengyicps9 优盟易9 
# 1238289 youmengyicps10 优盟易10 
# generateApk('1238280','youmengyicps6','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1238283','youmengyicps7','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1238285','youmengyicps8','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1238288','youmengyicps9','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1238289','youmengyicps10','街机水浒传','com.baiyikeji.jiejishuihuzhuan')


# generateApk('1519960','YY0906SHZ_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1519960','YY0906SHZ_APK','街机水浒传','com.arcadegame.shuihuzhuan')
# 1627742、1627743、1627744、1627745、1627746 
# generateApk('1627742','yawl1_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1627743','yawl2_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1627744','yawl3_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1627745','yawl4_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')

#1693503 1693505 1693508 1693509 1693511 
# generateApk('1693503','yawl6_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1693505','yawl7_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1693508','yawl8_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1693509','yawl9_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1693511','yawl10_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# 2017 3 15 周三 打的包
#百度竞价
# generateApk('1003689','bdgw01shz_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')

# generateApk('1050860','yiyouCPSshz_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')

# generateApk('1319134','shz_NTG_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1148873','yyscCPS_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')

# generateApk('1000058','gwshz_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1238269','youmengyicps11','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1000063','gwfxshz_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# generateApk('1113838','wuyuyu_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# #王者工会
# generateApk('1394096','WZGHCPS_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# #媒体安卓
# generateApk('1000375','mtshz_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# #玩游戏网 cps
# generateApk('1546801','wyxCPS_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# #宜推
# generateApk('1009362','ytshzcps_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
# #易昂网络4
# generateApk('1627746','yawl5_APK','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
#应用汇
# generateApk('1001201','yyhshz_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')

# generateApk('1841155','yxwcps_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')
generateApk('1856831','chengdufanyu_apk','街机水浒传','com.baiyikeji.jiejishuihuzhuan')

