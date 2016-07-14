
#coding=utf-8

"""
    此代码是用来下载上海数据开放平台的数据开放目录和机构的
"""

from getUrlData import getHtml
import re
import pickle
from saveFile import saveAsCSV
from saveFile import saveAsPKL
from dataClass import EntryData
from dataClass import Data

url = "http://www.datashanghai.gov.cn/query!"
#数据接口url
productPageUrl = "queryProduct.action?currentPage="
#应用接口url
appPageUrl = "queryApp.action?currentPage="
#接口信息url
interfacePageUrl = "queryInterface.action?currentPage="


#获取上海数据开放条目的总页数
def getTotalPage(url):
    #url = "http://www.datashanghai.gov.cn/query!queryProduct.action?currentPage=1"
    html = getHtml(url).decode('utf-8')
    reg = r"totalPage = '(\d{1,5})'"
    p = re.compile(reg)
    result = re.findall(p, html)
    return int(result[0])
#获取当前页面所有接口的连接
def getSHPageLinked(url):
    html = getHtml(url).decode('utf-8')
    start = int(html.find('class="list"'))
    end = int(html.find('id="pageSpan"'))
    content = html[start:end]
    reg = r'<a href="query!(.*)" title="(.*)" target=".*">(\s*.*){12}<strong class=".*">(.*)</strong></dt>'
    p = re.compile(reg)
    result = re.findall(p, content)
    return result

#获取改类型所有界面的连接
def getSHAllLinked(pageUrl, dataType, window):
    datalist = []
    totalPage = getTotalPage(url + pageUrl + str(1))
    window.systemPrint("正在下载"+ dataType+"连接,共" + str(totalPage) + "页")
    #print("正在下载"+ dataType+"连接,共" + str(totalPage) + "页")
    for page in range(currentPage, totalPage+1):
        window.systemPrint(u"正在下载第" + str(page) + u"页")
        #print(u"正在下载第" + str(page) + u"页")
        temp = getSHPageLinked(url + pageUrl + str(page))
        datalist.extend(temp)
    return datalist

#获取数据开放的详细信息
def getSHInfo(pageUrl, dataType, title):
    html = getHtml(url + pageUrl).decode('utf-8')
    reg = r'<td>(.*)\r*\s*</td>'
    sign = int(html.find('</table>'))
    p = re.compile(reg)
    result = re.findall(p,html[:sign])
    res = list(result)
    res.insert(0, title)
    res.insert(1, dataType)
    resStr = str(res)
    resStr = resStr.replace(' ', '')
    res = eval(resStr)
    return res

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




''''
#下载数据连接条目
#productLinkedList = getSHAllLinked(productPageUrl, "数据")
#appLinkedList = getSHAllLinked(appPageUrl, "应用")
interfaceLinkedList = getSHAllLinked(interfacePageUrl, "接口")

print('开始抓取数据')
ll = []
for each in interfaceLinkedList:
    print('|', end = '')
    ll.append(getSHInfo(each[0], each[3], each[1]))
#saveAsCSV(ll, "上海接口开放")

#ll = []
for each in productLinkedList:
    print('|', end = '')
    ll.append(getSHInfo(each[0], each[3], each[1]))
#saveAsCSV(ll, "上海数据开放")

#ll = []
for each in appLinkedList:
    print('|', end = '')
    ll.append(getSHInfo(each[0], each[3], each[1]))
#saveAsCSV(ll, "上海应用开放")
print('抓取数据成功')

#classList = []
#for each in ll:
#    temp = EntryData()
#    temp.setFromString(each[-2],each[1], each[0], 'SH')
#    classList.append(temp.getData())
classList = []
for each in infoList:
    temp = Data(each[-2],each[1], each[0], 'BJ')
    classList.append(temp)


print('数据分析中...')
saveAsPKL(classList, './data/SHEntry')
print('数据保存成功')


'''


#保存数据连接条目
#saveAsPickle("shanghaiProduct.pkl", productLinkedList)
#saveAsPickle("shanghaiApp.pkl", appLinkedList)
#saveAsPickle("shanghaiInterface.pkl", interfaceLinkedList)

