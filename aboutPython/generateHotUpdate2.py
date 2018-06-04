#coding=utf-8
import os,shutil
import sys
reload(sys)

#先将所有代码 编译成 luac

os.system('cocos luacompile -s /Users/lidongsheng/Documents/framework/hotupdate/ -d /Users/lidongsheng/Documents/framework/hotupdate/ -e -k MIIEpQIBAAKCAQEA5ANvIDDY1a+6bEb8LjW6e9HdcFIung -b DWC --disable-compile')

#将所有的 lua 代码删除
def removeLuafile(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith(str('.lua')):
				print 'remove 			', item
				os.remove(rootPath +"/"+item)
		elif(os.path.isdir(rootPath +"/"+item)):
			removeLuafile(rootPath +"/"+item)

removeLuafile('/Users/lidongsheng/Documents/framework/hotupdate/')


#生成所有开心电玩城的热更新文件；

#2.生成一个总游戏的 文件夹
#3.生成所有游戏的 zip 包
#4.删除总游戏的文件夹
def generateCopyFile(strPath):
	strArr = strPath.split('/')
	strPath2 = ''
	for i in range(0, len(strArr)):
		if(i==0):
			strPath2 = strPath2 +strArr[i]+'2'+'/'
		else:
			strPath2 = strPath2 +strArr[i]+'/'
	return strPath2

def copyFileToRoot2(keepPath):
	path = os.listdir(keepPath)
	for item in path:
		if (os.path.isfile(keepPath +"/"+item)):
			print 'move 			', item
			rootPath2 = generateCopyFile(keepPath)
			if(os.path.exists(rootPath2)==False):
				os.makedirs(rootPath2)
			shutil.move(keepPath +"/"+item,rootPath2+item)
		elif(os.path.isdir(keepPath +"/"+item)):
			copyFileToRoot2(keepPath +"/"+item)
#删除掉除指定路径下的其它文件夹及文件
def removeFileExceptPath(keepPath):
	rootPath = keepPath.split('/')[0]
	os.mkdir(rootPath+'2')
	copyFileToRoot2(keepPath)

	shutil.rmtree(rootPath)
	os.rename(rootPath+'2',rootPath)

# rootPath = raw_input('Enter a path :')
# strPath = str(rootPath)
# strPath = strPath.rstrip()
os.chdir('/Users/lidongsheng/Documents/framework/hotupdate/')
#1.生成一个dwc.zip
#创建一个 dwc 的文件夹

if (os.path.isdir('dwc')):
	shutil.rmtree('dwc')
	print '如果存在 dwc 文件夹那么就删除掉'
print('创建 dwc 文件夹')
os.mkdir(r'dwc')
print('将 src 和 res 复制到 dwc 文件夹')
shutil.copytree('src','dwc/src')
shutil.copytree('res','dwc/res')
print('开始删除掉 dwc/res 中游戏的【资源】')
if os.path.exists('dwc/res/Games'):
	shutil.rmtree('dwc/res/Games')
print('开始删除 dwc/src 中的游戏【代码】')
if os.path.exists('dwc/src/app/games'):
	shutil.rmtree('dwc/src/app/games')
print('开始删除 dwc/src 下的不需要的文件')

if os.path.exists('dwc/src/cocos'):
	os.remove('dwc/src/cocos')

if os.path.exists('dwc/src/app/modules/help'):
	os.remove('dwc/src/app/modules/help')

if os.path.exists('dwc/src/src.luaproj'):
	os.remove('dwc/src/src.luaproj')

if os.path.exists('dwc/src/src.config'):
	os.remove('dwc/src/src.config')

if os.path.exists('dwc/src/app/conf/BYConfig.luac'):
	os.remove('dwc/src/app/conf/BYConfig.luac')

if os.path.exists('dwc/src/app/conf/GameConfig.luac'):	
	os.remove('dwc/src/app/conf/GameConfig.luac')
	
print('移步到 dwc 文件夹')
os.chdir('dwc/')
os.system('zip -q -r dwc.zip *')
shutil.move('dwc.zip','../dwc.zip')
os.chdir('../')
shutil.rmtree('dwc')
print('----------------------------------------------完成dwc.zip')

# if(os.path.isdir('totalGames')):
# 	shutil.rmtree('totalGames')
# os.mkdir(r'totalGames')
# shutil.copytree('src','totalGames/src')
# shutil.copytree('res','totalGames/res')
# os.chdir('totalGames')
# removeFileExceptPath('src/app/games')
# removeFileExceptPath('res/Games')
# os.chdir('../')
# print('----------------------------------------------完成复制所有游戏资源')

# def generateGameZip(gameName,keepPath,keepPath2):

# 	if(os.path.isdir(gameName)):
# 		shutil.rmtree(gameName)

# 	shutil.copytree('totalGames/src',gameName+'/src')
# 	shutil.copytree('totalGames/res',gameName+'/res')
# 	os.chdir(gameName)
# 	if os.path.exists(keepPath):
# 		removeFileExceptPath(keepPath)
# 	if os.path.exists(keepPath2):
# 		removeFileExceptPath(keepPath2)
	
# 	os.system('zip -q -r '+gameName+'.zip *')
# 	shutil.move(gameName+'.zip','../'+gameName+'.zip')
# 	os.chdir('../')
# 	shutil.rmtree(gameName)
# 	print('----------------------------------------------完成'+gameName+'.zip')
# generateGameZip('bj','src/app/games/bj','res/Games/BJ')

# generateGameZip('brnn','src/app/games/brnn','res/Games/BRNN')

# generateGameZip('by','src/app/games/jjby','res/Games/JJBY')

# generateGameZip('by2','src/app/games/jjby','res/Games/QPBY')

# generateGameZip('fishrun','src/app/games/saiyu','res/Games/FishRun')

# generateGameZip('fruits','src/app/games/sgj','res/Games/SGJ')

# generateGameZip('roulette','src/app/games/roulette','res/Games/Roulette')

# generateGameZip('shz','src/app/games/shz','res/Games/SHZ')
# shutil.rmtree('totalGames')
