#!/usr/bin/env python
# encoding: utf-8
from biplist import *
from PIL import Image
import os
import json
from PIL import Image
import xml.dom.minidom
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readJSONFile(path):
	f = open(path)
	txt = f.read()
	jsonStr = str(txt)
	data = json.loads(jsonStr)
	doc = xml.dom.minidom.Document()
	root = doc.createElement('GameFile')
	doc.appendChild(root)

	PropertyGroup = doc.createElement('PropertyGroup')
	PropertyGroup.setAttribute('ID', str(data['ID']))
	PropertyGroup.setAttribute('Version', '2.3.3.0')
	PropertyGroup.setAttribute('Type', str(data['Type']))
	root.appendChild(PropertyGroup)

	OutContent = doc.createElement('Content')
	OutContent.setAttribute('ctype', 'GameProjectContent')
	root.appendChild(OutContent)

	Content = doc.createElement('Content')
	OutContent.appendChild(Content)
	# 动画这一块儿，由于水浒传中动画比较少，而且这一块反编译起来比较麻烦，暂时搁置
	AnimationData = data['Content']['Content']['Animation']
	Animation = doc.createElement('Animation')
	Animation.setAttribute('Duration', str(AnimationData['Duration']))
	Animation.setAttribute('Speed', str(AnimationData['Speed']))
	Content.appendChild(Animation)

	ObjectData = data['Content']['Content']['ObjectData']
	ObjectData_Node = doc.createElement('ObjectData')
	ObjectData_Node.setAttribute("Name", str(ObjectData['Name']))
	if 'Tag' in ObjectData:
		ObjectData_Node.setAttribute("Tag", str(ObjectData['Tag']))
	ObjectData_Node.setAttribute("ctype", str(ObjectData['ctype']))
	Content.appendChild(ObjectData_Node)

	Size = doc.createElement('Size')
	Size.setAttribute("X", str(ObjectData['Size']['X']))
	Size.setAttribute("Y", str(ObjectData['Size']['Y']))
	ObjectData_Node.appendChild(Size)

	Children = doc.createElement('Children')
	ObjectData_Node.appendChild(Children)
	if 'Children' in ObjectData:
		ChildrenArray = ObjectData['Children']
		for item in ChildrenArray:
			initOneNode(item, Children, doc)
	csdFileName = str.replace(path, '.json', '.csd')
	f = open(csdFileName, 'w')
	f.write(doc.toprettyxml(indent='\t', newl='\n', encoding='utf-8'))
	f.close()

def initOneNode(item, Children, doc):
	AbstractNodeData = doc.createElement('AbstractNodeData')
	Children.appendChild(AbstractNodeData)

	for tag in item:
		if (str(item['ctype']) == 'ImageViewObjectData' or str(item['ctype']) == 'ButtonObjectData') and str(tag) == 'Scale9OriginX':
			AbstractNodeData.setAttribute('LeftEage', str(item['Scale9OriginX']))
			imageFileData = 'FileData'
			if item['ctype'] == 'ImageViewObjectData':
				imageFileData = 'FileData'
			elif item['ctype'] == 'ButtonObjectData':
				imageFileData = 'NormalFileData'
			if item[imageFileData]['Plist'] != '':
				plistFile = readPlist(item[imageFileData]['Plist'])
				imageName = item[imageFileData]['Path']
				sourceSize = plistFile['frames'][imageName]['sourceSize'].replace('{','').replace('}','').split(',')
				imageWidth = float(sourceSize[0])
				print(type(imageWidth),imageWidth)
				AbstractNodeData.setAttribute('RightEage', str(imageWidth - item['Scale9OriginX'] - item['Scale9Width']))
			else:
				img = Image.open(item[imageFileData]['Path'])
				imageWidth = float(img.size[0])
				AbstractNodeData.setAttribute('RightEage', str(imageWidth - item['Scale9OriginX'] - item['Scale9Width']))
		elif (item['ctype'] == 'ImageViewObjectData' or item['ctype'] == 'ButtonObjectData') and tag == 'Scale9OriginY':
			AbstractNodeData.setAttribute('TopEage', str(item['Scale9OriginY']))
			imageFileData = 'FileData'
			if item['ctype'] == 'ImageViewObjectData':
				imageFileData = 'FileData'
			elif item['ctype'] == 'ButtonObjectData':
				imageFileData = 'NormalFileData'
			if item[imageFileData]['Plist'] != '':
				plistFile = readPlist(item[imageFileData]['Plist'])
				imageName = item[imageFileData]['Path']
				sourceSize = plistFile['frames'][imageName]['sourceSize'].replace('{','').replace('}','').split(',')
				imageHeight = float(sourceSize[1])
				AbstractNodeData.setAttribute('BottomEage', str(imageHeight - item['Scale9OriginY'] - item['Scale9Height']))
			else:
				img = Image.open(item[imageFileData]['Path'])
				imageHeight = float(img.size[1])
				AbstractNodeData.setAttribute('BottomEage', str(imageHeight - item['Scale9OriginY'] - item['Scale9Height']))
		elif tag == 'CColor' or tag == 'ShadowColor':
			xmlNode = doc.createElement(tag)
			xmlNode.setAttribute('A', '255')
			xmlNode.setAttribute('R', '255')
			xmlNode.setAttribute('G', '255')
			xmlNode.setAttribute('B', '255')
			for key in item[tag]:
				xmlNode.setAttribute(key, str(item[tag][key]))
			AbstractNodeData.appendChild(xmlNode)
		elif tag == 'Children':
			xmlNode = doc.createElement(tag)
			for subItem in item['Children']:
				initOneNode(subItem, xmlNode, doc)
		elif not isinstance(item[tag], dict):
			AbstractNodeData.setAttribute(tag, str(item[tag]))
		else:
			addOneChildSubNode(AbstractNodeData, tag, item[tag], doc)


def addOneChildSubNode(Children, mKey, item, doc):
	xmlNode = doc.createElement(mKey)
	for i in item:
		xmlNode.setAttribute(i, str(item[i]))
	Children.appendChild(xmlNode)

def generateCSD(rootPath):
	path = os.listdir(rootPath)
	for item in path:
		if os.path.isfile(rootPath + "/"+item):
			if item.endswith('.json'):
				print(rootPath + "/"+item)
				readJSONFile(rootPath + "/"+item)
		elif os.path.isdir(rootPath + "/"+item):
			generateCSD(rootPath + "/"+item)


os.chdir('/Users/lidongsheng/Desktop/json')
generateCSD('/Users/lidongsheng/Desktop/json')
