#coding:utf-8
import os,shutil

print "js-->jsc"
os.chdir('/Users/lidongsheng/Documents/ShuiHuZhuan2')
# os.system('cocos jscompile -s src -d src')

def moveLuafile(rootPath,otherPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith('.js'):
				arrR = rootPath.split("/")
				strC = ""
				for num in range(1,len(arrR)):
					strC = strC+"/"+arrR[num]
				strC = otherPath+strC
				print strC
				if not (os.path.isdir(strC)):
					os.makedirs(strC)
				shutil.move(rootPath +"/"+item,strC)
		elif(os.path.isdir(rootPath +"/"+item)):
			moveLuafile(rootPath +"/"+item,otherPath)
strPath = 'src'

oPath = '../shuiHuZhuanSrcCopy'

print('js copy')
moveLuafile(strPath,oPath)
# os.system('cocos compile -p android -m release')
isRevert = raw_input("Do you want to revert ? y/n :")
if(isRevert=='y'):
	moveLuafile(oPath,strPath)	
	print "file have revert"