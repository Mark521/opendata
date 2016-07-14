
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
