import json
f = open('/Users/lidongsheng/Desktop/json/Modules/Chat/byChatNode.json')
txt = f.read()
jsonStr = str(txt)
data = json.loads(jsonStr)
jsonArray = data['Content']['Content']['ObjectData']['Children'][1]
for i in jsonArray:
	print(i)
	print(type(jsonArray[i]))
