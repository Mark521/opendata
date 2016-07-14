#coding=utf-8

import urllib.request

#获取特定Url的数据
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


#url = "http://www.datashanghai.gov.cn/query!queryGdsDataInfoById.action?type=0&dataId=AB9002015061"
#html = getHtml(url)

#with open("index.txt", "wb") as f:
#    f.write(html)
