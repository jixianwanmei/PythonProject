# encoding: utf-8
import os,shutil
def baseFileName(path):
	return path.split('/')[-1]


def renamePngInFile(path,suffix,newName,oldName):
	for item in path:
		if (os.path.isfile(path +"/"+item)):
			if item.endswith(str(suffix)):
				print 'rename 			', item
				os.remove(rootPath +"/"+item)
				name1 = item.split('.')[0]+'2.'+suffix
				f1 = open(path+'/'+item)
				f2 = open(name1,'w')
				for s in f1.readlines():
					f2.write(s.replace(newName,oldName))
				f1.close()
				f2.close()
				os.remove(path+'/'+item)
				os.rename(path+'/'+name1,item)
		elif(os.path.isdir(path +"/"+item)):
			renamePngInFile(path +"/"+item,suffix,newName,oldName)

def renamePng(path):
	mFileName = baseFileName(path)
	os.rename(path,'change_'+mFileName)

	name1 = mFileName.split('.')[0]
	if os.path.exists(name1+'.plist'):

		# 首先将 plist 文件中的 png 字段改成修改过的
		f1 = open(name1+'.plist')
		f2 = open(name1+'2.plist','w')

		for s in f1.readlines():
			f2.write(s.replace('change_'+mFileName,mFileName))
		f1.close()
		f2.close()
		os.remove(name1+'.plist')
		os.rename(name1+'.plist',name1+'2.plist')


		path2 = path.split('.')[0]+'.plist'
		os.rename(path2,'change_'+name1+'.plist')
		# 修改 
		renamePngInFile('res','.json',path2,name1+'.plist')
	else:
		renamePngInFile('res','.json',name1+'/change_'+mFileName,path)
os.chdir('../../ShuiHuZhuan')		
renamePng('res/shz/GameHall/DT_caidan.png')
	