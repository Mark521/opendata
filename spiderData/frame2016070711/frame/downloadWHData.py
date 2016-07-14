
#coding=utf-8

"""
    此代码是用来下载武汉数据开放平台的数据开放目录和机构的
"""

from getUrlData import getHtml
import re
import pickle
import json
import os
from saveFile import saveAsPKL
from dataClass import EntryData

#获取武汉数据开放条目的id
def getResourceId(url):
    html = getHtml(url).decode('utf-8')
    sign = int(html.find('25bde262-31b4-4901-8d53-527631005f6a'))
    start = int(html.find("<div", sign))
    end = int(html.find("</div>", sign))
    resource = html[start:end]
    sign = int(html.find('60d79024-a7f3-4c73-8b78-b7153fa1f1aa'))
    start = int(html.find("<div", sign))
    end = int(html.find("</div>", sign))
    orgenization = html[start:end]
    reg = r'<a href=".*" id="(.*)" class="list-group-item text-center" title=".*">([\u4e00-\u9fa5]*)</a>'
    p = re.compile(reg)
    orgResult = re.findall(p, orgenization)
    resResult = re.findall(p, resource)
    return orgResult, resResult
#获取当前页面所有接口的连接
def getWHAllPageLinked(url):
    html = getHtml(url).decode('utf-8')
    data = json.loads(html)
    return data

#对当前获取json数据进行分析
def getWHInfoFromJson(data):
    reg = '<ResourceName>(.*)<\/ResourceName><DataShape>(.*)<\/DataShape>.*<ResourceType>(.*)<\/ResourceType>.*<OrganizationName>(.*)<\/OrganizationName>'
    p = re.compile(reg)
    resultList = []
    for each in data:
        root = each['metadata']
        result = re.findall(p, root)
        resultList.extend(result)
    return resultList
        
#获取数据开放的详细信息
def getWHInfo(pageUrl):
    html = getHtml(url + pageUrl).decode('utf-8')
    reg = r'<td>\s*(\w*)\r*\s*</td>'
    p = re.compile(reg)
    result = re.findall(p,html)
    return result

#保存列表信息
def saveAsPickle(fileName, data):
    with open(fileName, 'wb') as f:
        pickle.dump(data, f)

#武汉数据开放列表的总页面
listUrl = 'http://www.wuhandata.gov.cn/whdata/resources_listPage.action'
infoUrl = 'http://www.wuhandata.gov.cn/whdata/resources_list.action?category=25bde262-31b4-4901-8d53-527631005f6a&pageNum='

#获取数据开放的条目,包括开放机构和开放项目
orgResult, resResult = getResourceId(listUrl)

#用于存储各个数据开放的条目
dataList = []
'''
#对数据也进行循环读取
page = 1
dataInfo = getAllPageLinked(infoUrl + str(page))
totlePage = dataInfo['pages']
dataList.extend(getInfoFromJson(dataInfo['list']))
while(dataInfo['hasNextPage'] == True):
    page = page + 1
    print('共'+str(totlePage)+'页,当天正在下载第' +str(page) + "页" )
    dataInfo = getAllPageLinked(infoUrl + str(page))
    dataList.extend(getInfoFromJson(dataInfo['list']))


#将所有信息保存到类中
classList = []
for each in dataList:
    temp = Data(each[3],each[2], each[0], 'WH')
    classList.append(temp)
print('数据分析中...')
saveAsPKL(classList, './data/WHEntry')
print('数据保存成功')'''
