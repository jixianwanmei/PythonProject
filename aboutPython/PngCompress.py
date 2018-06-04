#coding:utf-8
import os
import os.path
import sys
import string
import ConfigParser
# rootPath = raw_input('请输入需要压缩图片的根目录 :')
# strPath = str(rootPath)
# strPath = strPath.rstrip()
#
# def recursionFindPng(rootPath):
# 	path = os.listdir(rootPath)
# 	for item in path:
# 		if (os.path.isfile(rootPath +"/"+item)):
# 			if item.endswith('.png'):
# 				print 'remove 			', item
# 				compressImg(rootPath +"/"+item)
# 		elif(os.path.isdir(rootPath +"/"+item)):
# 			recursionFindPng(rootPath +"/"+item)
#
# def compressImg(filePath):
#
os.system('pngquant --force --speed=1 --quality=20-60 -v /Users/lidongsheng/Downloads/testCompress/abc.png -o /Users/lidongsheng/Downloads/output/abc.png')

