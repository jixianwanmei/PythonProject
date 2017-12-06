#coding=utf-8
#将所有的 A 文件夹（包括子文件夹）下的指定类型文件复制到
#B 文件夹下的同一路径下
#比如 A/game/c.png 复制到 B/game/c.png 
#如果 B/game/c.png 存在则替换掉

import os,shutil
os.chdir('../../')
rootPath1 = 'framework'
rootPath2 = 'framework2'
def findFile(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith('.png') or item.endswith('.jpg') :
				pngPath = rootPath +"/"+item
				if item.endswith('.png'):
					plistItem = pngPath.replace('png','plist')
					dstPath = pngPath.replace(rootPath1,rootPath2,1)
					if not os.path.isfile(plistItem):
						if not os.path.isfile(dstPath):
							print dstPath + 'is the new files dont contains file'
						shutil.copy( pngPath, dstPath)
				else:
					dstPath = pngPath.replace(rootPath1,rootPath2)
					if not os.path.isfile(dstPath):
						print dstPath + 'is the new files dont contains file'
					shutil.copy(pngPath, dstPath)
		elif(os.path.isdir(rootPath +"/"+item)):
			findFile(rootPath +"/"+item)
strPath = str(rootPath1)
strPath = strPath.rstrip()
print strPath +'is the filePath to remove '
findFile(strPath)