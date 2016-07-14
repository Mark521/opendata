
#coding=utf-8

"""
    此代码是用来下载北京数据开放平台的数据开放目录和机构的
"""

from getUrlData import getHtml
import re
import pickle
from saveFile import saveAsPKL
from dataClass import EntryData
from dataClass import Data

#获取北京数据开放机构的名称和链接
def getFromGov(url):
    html = getHtml(url).decode('utf-8')
    sign = int(html.find('ess_ctr506_OrganizationsListTree_divDataOrg'))
    start = int(html.find('<ul>', sign))
    end = int(html.find('</ul>', sign))
    content = html[start:end]
    reg = r'<a href="../(.*)">(.*)（(\d*)）</a>'
    p = re.compile(reg)
    result = re.findall(p, content)
    return result

#获取北京数据开放主题的条目和链接
def getFromSubject(url):
    html = getHtml(url).decode('utf-8')
    sign = int(html.find('ess_ctr473_contentpane'))
    start = int(html.find('<ul', sign))
    end = int(html.find('</div>', sign))
    content = html[start:end]
    reg = r''
    p = re.compile(reg)
    result = re.findall(p, content)
    return content

#获取当前页面所有接口的连接
def getPageLinked(url, jg):
    html = getHtml(url).decode('utf-8')
    reg = r'<a id=".*" class="hylName" href=".*">(.*)</a>(.*\s*){2}(.*)\r'
    p = re.compile(reg)
    result = re.findall(p, html)
    res = []
    for each in result:
        tempList = []
        tempList.append(each[0])
        tempList.append(each[2].replace(' ', ''))
        tempList.append(jg)
        res.append(tempList)
    return res

#获取数据开放的详细信息
def getInfo(pageUrl):
    html = getHtml(pageUrl).decode('utf-8')
    reg = r'<span id=".*" class="indent">(.*)</span>'
    p = re.compile(reg)
    result = re.findall(p,html)
    return result

#保存列表信息
def saveAsPickle(fileName, data):
    with open(fileName, 'wb') as f:
        pickle.dump(data, f)

#北京数据按主题划分的界面数据
aztUrl = "http://www.bjdata.gov.cn/zyml/azt/lyzs/zs/index.htm"
#北京数据按机构划分的界面数据
ajgUrl = "http://www.bjdata.gov.cn/zyml/ajg/"
#获取所有开放数据的政府机构
result = getFromGov(ajgUrl + "sjw/index.htm")
result.insert(0,('sjw/index.htm', '市教委', '6'))
#获取北京开放数据的种类进行,按主题进行保存
content = getFromSubject(aztUrl)

#print(getPageLinked('http://www.bjdata.gov.cn/zyml/ajg/sjw/index.htm'))

#print(getInfo('http://www.bjdata.gov.cn/zyml/ajg/sjw/3350.htm'))
infoList = []
for each in result:
    temp = getPageLinked(ajgUrl + each[0], each[1])
    if(int(each[2])> 20):
        tempUrl = ''
        tempUrl = '' + ajgUrl + each[0]
        tempss = tempUrl[:-4] + '1.htm'
        temp.extend(getPageLinked(tempss, each[1]))
    print(len(temp), each[1])
    infoList.extend(temp)

#将所有信息保存到类中
classList = []
for each in infoList:
    temp = Data(each[2],each[1], each[0], 'BJ')
    classList.append(temp)
print('数据分析中...')
saveAsPKL(classList, './data/BJEntry')
print('数据保存成功')
