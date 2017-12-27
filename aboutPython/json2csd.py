#!/usr/bin/env python
# encoding: utf-8
from biplist import *
from PIL import Image
import os
import json
from PIL import Image
import xml.dom.minidom
doc = xml.dom.minidom.Document()
os.chdir('/Users/lidongsheng/Documents/ShuiHuZhuan/res')
def readJSONFile(path):
	f = open(path)
	txt = f.read()
	jsonStr = str(txt)
	data = json.loads(jsonStr)
	csdFileName = data['Name']

	root = doc.createElement('GameFile')
	doc.appendChild(root)

	PropertyGroup = doc.createElement('PropertyGroup')
	PropertyGroup.setAttribute('ID', data['ID'])
	PropertyGroup.setAttribute('Version', '2.3.3.0')
	PropertyGroup.setAttribute('Type', data['Type'])
	root.appendChild(PropertyGroup)

	OutContent = doc.createElement('Content')
	OutContent.setAttribute('ctype', 'GameProjectContent')
	root.appendChild(OutContent)

	Content = doc.createElement('Content')
	OutContent.appendChild(Content)
	# 动画这一块儿，由于水浒传中动画比较少，而且这一块反编译起来比较麻烦，暂时搁置
	AnimationData = data['Content']['Content']['Animation']
	Animation = doc.createElement('Animation')
	Animation.setAttribute('Duration', AnimationData['Duration'])
	Animation.setAttribute('Speed', AnimationData['Speed'])
	Content.appendChild(AnimationData)

	ObjectData = data['Content']['Content']['ObjectData']
	ObjectData_Node = doc.createElement('ObjectData')
	ObjectData_Node.setAttribute("Name", ObjectData['Name'])
	ObjectData_Node.setAttribute("Tag", ObjectData['Tag'])
	ObjectData_Node.setAttribute("ctype", ObjectData['ctype'])
	Content.appendChild(ObjectData_Node)

	Size = doc.createElement('Size')
	Size.setAttribute("X", ObjectData['Size']['X'])
	Size.setAttribute("Y", ObjectData['Size']['Y'])
	ObjectData_Node.appendChild(Size)

	Children = doc.createElement('Children')
	ObjectData_Node.appendChild(Children)

	ChildrenArray = ObjectData['Children']
	for item in ChildrenArray:
		initOneNode(item,Children)
def initOneNode(item, Children):
	ctype = item['ctype']
	AbstractNodeData = doc.createElement('AbstractNodeData')

	AbstractNodeData.setAttribute('ctype', item['ctype'])
	AbstractNodeData.setAttribute('Name', item['Name'])
	AbstractNodeData.setAttribute('ActionTag', item['ActionTag'])
	AbstractNodeData.setAttribute('Tag', item['Tag'])
	AbstractNodeData.setAttribute('IconVisible', item['IconVisible'])
	AbstractNodeData.setAttribute('LeftMargin', item['LeftMargin'])
	AbstractNodeData.setAttribute('RightMargin', item['RightMargin'])
	AbstractNodeData.setAttribute('TopMargin', item['TopMargin'])
	AbstractNodeData.setAttribute('BottomMargin', item['BottomMargin'])
	if ctype == 'ImageViewObjectData':
		AbstractNodeData.setAttribute('Scale9Enable', item['Scale9Enable'])
		if item['Scale9Enable']:
			AbstractNodeData.setAttribute('TopEage', item['Scale9OriginX'])
			AbstractNodeData.setAttribute('LeftEage', item['Scale9OriginY'])
			AbstractNodeData.setAttribute('Scale9Width', item['Scale9Width'])
			AbstractNodeData.setAttribute('Scale9Height', item['Scale9Height'])
			if item['FileData']['Plist'] != '':
				plistFile = readPlist(item['FileData']['Plist'])
				imageName = item['FileData']['Path']
				imageWidth = plistFile['frames'][imageName]['sourceSize'][0]
				imageHeight = plistFile['frames'][imageName]['sourceSize'][1]
                AbstractNodeData.setAttribute('BottomEage', imageWidth - item['Scale9OriginX'] - item['Scale9Width'])
                AbstractNodeData.setAttribute('RightEage', imageHeight - item['Scale9OriginY'] - item['Scale9Height'])
            else:
                img = Image.open(item['FileData']['Path'])
				imageWidth = img.size[0]
				imageHeight = img.size[1]
				AbstractNodeData.setAttribute('BottomEage', imageWidth - item['Scale9OriginX'] - item['Scale9Width'])
				AbstractNodeData.setAttribute('RightEage', imageHeight - item['Scale9OriginY'] - item['Scale9Height'])
		addOneChildSubNode(AbstractNodeData, 'Size', item['Size'])
		addOneChildSubNode(AbstractNodeData, 'AnchorPoint', item['AnchorPoint'])
		addOneChildSubNode(AbstractNodeData, 'Position', item['Position'])
		addOneChildSubNode(AbstractNodeData, 'Scale', item['Scale'])

		CColor= doc.createElement('CColor')
		CColor.setAttribute('A','255')
		CColor.setAttribute('R','255')
		CColor.setAttribute('G','255')
		CColor.setAttribute('B','255')
		for key in item['CColor']:
			CColor.setAttribute(key, item['CColor'][key])
		Children.appendChild(CColor)

		addOneChildSubNode(AbstractNodeData, 'PrePosition', item['PrePosition'])
		addOneChildSubNode(AbstractNodeData, 'PreSize', item['PreSize'])
		addOneChildSubNode(AbstractNodeData,'FileData',item['FileData'])
        elif ctype = 'TextObjectData':
		    AbstractNodeData.setAttribute('FontSize', item['FontSize'])
		    AbstractNodeData.setAttribute('LabelText', item['LabelText'])
		    AbstractNodeData.setAttribute('OutlineSize', item['OutlineSize'])
		    if item.has_key('HorizontalAlignmentType'):
		    	AbstractNodeData.setAttribute('HorizontalAlignmentType', item['HorizontalAlignmentType'])
    		if item.has_key('VerticalAlignmentType'):
		    	AbstractNodeData.setAttribute('VerticalAlignmentType', item['VerticalAlignmentType'])
		    if item.has_key('OutlineEnabled'):
		    	AbstractNodeData.setAttribute('OutlineEnabled', item['OutlineEnabled'])
		    if item.has_key('ShadowOffsetX'):
		    	AbstractNodeData.setAttribute('ShadowOffsetX', item['ShadowOffsetX'])
		    if item.has_key('ShadowOffsetY'):
		    	AbstractNodeData.setAttribute('ShadowOffsetY', item['ShadowOffsetY'])
		    if item.has_key('IsCustomSize'):
		    	AbstractNodeData.setAttribute('IsCustomSize', item['IsCustomSize'])
		    AbstractNodeData.setAttribute('TouchEnable', item['TouchEnable'])	
			addOneChildSubNode(AbstractNodeData, 'Size', item['Size'])
			addOneChildSubNode(AbstractNodeData, 'AnchorPoint', item['AnchorPoint'])
			addOneChildSubNode(AbstractNodeData, 'Position', item['Position'])
			addOneChildSubNode(AbstractNodeData, 'Scale', item['Scale'])
		    
		if item.has_key['Children']:
			initOneNode(item['Children'],AbstractNodeData)
		    
		    

def addOneChildSubNode(Children,mKey,item):
	xmlNode = doc.createElement(mKey)
	for i in item:
		xmlNode.setAttribute(i,item[i])
	Children.appendChild(xmlNode)
