# encoding: utf-8
#coding:utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
from langconv import *
# 转换繁体到简体

def doConvertFans(fileName):
	print 'fileName : ' + fileName
	f1 = open(fileName)
	fileName2 = fileName.split('.')[0] + 'Copy.' + fileName.split('.')[1]
	print 'fileName2 : ' + fileName2
	f2 = open(fileName2,'w')
	for s in f1.readlines():
		s2 = Converter('zh-hant').convert(s.decode('utf-8'))
		f2.write(str(s2))
	f1.close()
	f2.close()
	os.remove(fileName)
	os.rename(fileName2,fileName)

rootPath = raw_input('Enter a path :')
suffix = raw_input('Enter a suffix :')
#转换繁体字
def convertFans(rootPath,suffix):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith(suffix):
				print 'remove 			', item
				doConvertFans(rootPath +"/"+item)
		elif(os.path.isdir(rootPath +"/"+item)):
			convertFans(rootPath +"/"+item,suffix)

strPath = str(rootPath)
strSuffix = str(suffix)
strPath = strPath.rstrip()
print strPath +'is the filePath to convert '
convertFans(strPath,strSuffix)


# line = '123金币'
# 转换简体到繁体
# line = Converter('zh-hant').convert(line.decode('utf-8'))
# line = line.encode('utf-8')
# print line