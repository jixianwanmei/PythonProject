#!/usr/bin/env python
from biplist import *
plistFile = readPlist('/Users/lidongsheng/Documents/ShuiHuZhuan/res/shz/login/dengLu.plist')
print(plistFile)
for i in plistFile:
	print('key: ' + i)
	print(plistFile[i])
	print('----------------------')