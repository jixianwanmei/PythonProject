 #coding:utf-8
import os
import os.path
import sys
import string
import ConfigParser
# rootPath = raw_input('./compress')
# strPath = str(rootPath)
strPath = './compress'

def recursionFindPng(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith('.png'):
				print 'remove 			', item
				terminalCommand = './pngquant --force --speed=1 --quality=50-90 -v '
				pngPath = rootPath +"/"+item
				os.system(terminalCommand+pngPath+' -o'+pngPath)
		elif(os.path.isdir(rootPath +"/"+item)):
			recursionFindPng(rootPath +"/"+item)


recursionFindPng(strPath)
# os.system('./pngquant --force --speed=1 --quality=50-90 -v /Users/lidongsheng/Downloads/testCompress/abc.png -o /Users/lidongsheng/Downloads/output/abc.png')

