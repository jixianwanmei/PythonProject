# python ChangeImageSize.py filePaths
import Image
import os
import sys
def changeImageSize(imageFile):
	im = Image.open(imageFile)
	(x, y) = im.size  # read image size
	scaleRate = 1334 / 1136.0
	x_s = int(x * scaleRate)  # define standard width
	y_s = int(y * scaleRate)  # calc height based on standard width
	out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
	out.save(imageFile,quality = 100)

	print 'original size: ', x, y
	print 'adjust size: ', x_s, y_s
	print imageFile

def findImage(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if (os.path.isfile(rootPath +"/"+item)):
			if item.endswith('.png'):
				print 'remove 			', item
				changeImageSize(rootPath +"/"+item)
		elif(os.path.isdir(rootPath +"/"+item)):
			findImage( rootPath + "/" + item )


strPath = str( sys.argv[1] )
strPath = strPath.rstrip()
findImage( strPath )