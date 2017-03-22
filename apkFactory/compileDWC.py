# encoding: utf-8
import os,shutil
import xlrd
import sys
reload(sys)
def generateApk(channelID,nameStr):
	os.chdir('../../framework/src/app/conf')
	f1 = open('BYConfig.lua')
	f2 = open('BYConfig2.lua','w')
	for s in f1.readlines():
		f2.write(s.replace('20021',channelID))
	f1.close()
	f2.close()
	os.remove('BYConfig.lua')
	os.rename('BYConfig2.lua','BYConfig.lua')
	os.chdir('../../../')
	# 更改安卓渠道号；
	os.chdir('frameworks/runtime-src/proj.android')

	f1 = open('AndroidManifest.xml')
	f2 = open('AndroidManifest2.xml','w')
	for s in f1.readlines():
		f2.write(s.replace('20021',channelID))
	f1.close()
	f2.close()
	os.remove('AndroidManifest.xml')
	os.rename('AndroidManifest2.xml','AndroidManifest.xml')
	os.chdir('../../../')

	os.system('cocos compile -p android -m release ')
	os.chdir('publish/android/')
	os.rename('GameFramework-release-signed.apk',nameStr+'.apk')
	os.system('open . ')
	os.chdir('../../src/app/conf')
	#打完包以后把渠道id再改回来方便下次替换
	f1 = open('BYConfig.lua')
	f2 = open('BYConfig2.lua','w')
	for s in f1.readlines():
		f2.write(s.replace(channelID,'20021'))
	f1.close()
	f2.close()
	os.remove('BYConfig.lua')
	os.rename('BYConfig2.lua','BYConfig.lua')
	os.chdir('../../../')
	os.chdir('frameworks/runtime-src/proj.android')

	f1 = open('AndroidManifest.xml')
	f2 = open('AndroidManifest2.xml','w')
	for s in f1.readlines():
		f2.write(s.replace(channelID,'20021'))
	f1.close()
	f2.close()
	os.remove('AndroidManifest.xml')
	os.rename('AndroidManifest2.xml','AndroidManifest.xml')

	os.chdir('../../../../PythonProject/apkFactory')
	print '-----------------------------------------------完成一个apk'

#20022、20023、20024、20025、20026、20027 	
# generateApk('20022','UMY20022')
# generateApk('20023','UMY20023')
# generateApk('20024','UMY20024')
# generateApk('20025','UMY20025')
# generateApk('20026','UMY20026')
# generateApk('20027','UMY20027')
generateApk('20002','UMY20002')