# coding:utf-8
import urllib, urllib2, base64 ,json


access_token = '24.66a3616f4a9cceab0f6906794d94e32f.2592000.1517990707.282335-10652197'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'/Users/lidongsheng/Desktop/Lua中文教程-7.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
params = urllib.urlencode(params)
request = urllib2.Request(url, params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print(content)
    jsonData = json.loads(content)
    words_result = jsonData['words_result']
    wordAllWidth = 0
    wordAllCount = 0
    for item in words_result:
        wordWidth = item['location']['width']
        wordCount = len(item['words'])
        if wordCount >=4:
            wordAllWidth = wordAllWidth + wordWidth
            wordAllCount = wordAllCount + wordCount
    avgWidth = wordAllWidth / (wordAllCount * 1.0)
    print(avgWidth)