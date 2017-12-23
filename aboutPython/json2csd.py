# encoding: utf-8
import json
import xml.dom.minidom
def readJSONFile(path):
	f = open(path)
	txt = f.read()
	jsonStr = str(txt)
	data = json.loads(jsonStr)
	csdFileName = data['Name']

	doc = xml.dom.minidom.Document() 
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
	#动画这一块儿，由于水浒传中动画比较少，而且这一块反编译起来比较麻烦，暂时搁置
	AnimationData = data['Content']['Content']['Animation']
	Animation = doc.createElement('Animation')
	Animation.setAttribute（'Duration',AnimationData['Duration']）
	Animation.setAttribute（'Speed',AnimationData['Speed']）
	Content.appendChild(AnimationData)

	ObjectData = data['Content']['Content']['ObjectData']
	ObjectData_Node = doc.createElement('ObjectData')
	ObjectData_Node.setAttribute("Name",ObjectData['Name'])
	ObjectData_Node.setAttribute("Tag",ObjectData['Tag'])
	ObjectData_Node.setAttribute("ctype",ObjectData['ctype'])
	Content.appendChild(ObjectData_Node)

	Size = doc.createElement('Size')
	Size.setAttribute("X",ObjectData['Size']['X'])
	Size.setAttribute("Y",ObjectData['Size']['Y'])
	ObjectData_Node.appendChild(Size)

	Children = doc.createElement('Children')
	ObjectData_Node.appendChild(Children)

	ChildrenArray = ObjectData['Children']
	for item in ChildrenArray:
		initOneNode(item)
def initOneNode(item,Children):
	ctype = item['ctype']
	AbstractNodeData = doc.createElement('AbstractNodeData')
	if(ctype == 'ImageViewObjectData'):
		AbstractNodeData.setAttribute('')
		Size = doc.createElement('Size')





	