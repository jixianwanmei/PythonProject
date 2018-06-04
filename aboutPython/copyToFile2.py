#coding:utf-8
import os,shutil
import sys
reload(sys)
def copyfile(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith(str(".ogg")):
				print 'remove 			', item
				srcFile = rootPath +"/"+item
				dstFile = srcFile.replace("framework2","framework")
				dstFile = dstFile.replace(item,"")
				shutil.copy(rootPath +"/"+item,dstFile)
		elif(os.path.isdir(rootPath +"/"+item)):
			copyfile(rootPath +"/"+item)
os.chdir('../../')
copyfile('framework2/cocosstudio')
