#coding:utf-8
import os
import re
rootPath = raw_input('Enter a path :')
fileSuffix = raw_input('Enter a suffix :')
def removeLuafile(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith(str(fileSuffix)):
				print 'remove 			', item
				os.remove(rootPath +"/"+item)
		elif(os.path.isdir(rootPath +"/"+item)):
			removeLuafile(rootPath +"/"+item)


strPath = str(rootPath)
strPath = strPath.rstrip()
print strPath +'is the filePath to remove '
removeLuafile(strPath)