
#coding=utf-8

"""
    此代码是用来下载上海数据开放平台的数据开放目录和机构的
"""

from getUrlData import getHtml
import re
import pickle


#获取上海数据开放条目的总页数
def getTotalPage(url):
    #url = "http://www.datashanghai.gov.cn/query!queryProduct.action?currentPage=1"
    html = getHtml(url).decode('utf-8')
    reg = r"totalPage = '(\d{1,5})'"
    p = re.compile(reg)
    result = re.findall(p, html)
    return int(result[0])
#获取当前页面所有接口的连接
def getPageLinked(url):
    html = getHtml(url).decode('utf-8')
    start = int(html.find('class="list"'))
    end = int(html.find('id="pageSpan"'))
    content = html[start:end]
    reg = r'<a href="query!(.*)" title='
    p = re.compile(reg)
    result = re.findall(p, content)
    return result

#获取改类型所有界面的连接
def getAllLinked(pageUrl, dataType):
    datalist = []
    totalPage = getTotalPage(url + pageUrl + str(1))
    print("正在下载"+ dataType+"连接,共" + str(totalPage) + "页")
    for page in range(currentPage, totalPage+1):
        print(u"正在下载第" + str(page) + u"页")
        temp = getPageLinked(url + pageUrl + str(page))
        datalist.extend(temp)
    return datalist

#获取数据开放的详细信息
def getInfo(pageUrl):
    html = getHtml(url + pageUrl).decode('utf-8')
    reg = r'<td>\s*(\w*)\r*\s*</td>'
    p = re.compile(reg)
    result = re.findall(p,html)
    return result

#保存列表信息
def saveAsPickle(fileName, data):
    with open(fileName, 'wb') as f:
        pickle.dump(data, f)

url = "http://www.datashanghai.gov.cn/query!"
#数据接口url
productPageUrl = "queryProduct.action?currentPage="
#应用接口url
appPageUrl = "queryApp.action?currentPage="
#接口信息url
interfacePageUrl = "queryInterface.action?currentPage="

currentPage = 1
#数据接口url
productLinkedList = []
#应用接口url
appLinkedList = []
#接口信息url
interfaceLinkedList = []

#下载数据连接条目
productLinkedList = getAllLinked(productPageUrl, "数据")
appLinkedList = getAllLinked(appPageUrl, "应用")
interfaceLinkedList = getAllLinked(interfacePageUrl, "接口")



#保存数据连接条目
saveAsPickle("shanghaiProduct.pkl", productLinkedList)
saveAsPickle("shanghaiApp.pkl", appLinkedList)
saveAsPickle("shanghaiInterface.pkl", interfaceLinkedList)

