#coding:utf-8
import os,shutil
import sys
reload(sys)
def copyfile(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith(str(".csd")):
				print rootPath +"/"+item 
		elif(os.path.isdir(rootPath +"/"+item)):
			copyfile(rootPath +"/"+item)
os.chdir('../../')
copyfile('framework2/')
