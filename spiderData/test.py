import re
import pickle
import csv
from getUrlData import getHtml
import xml.etree.ElementTree
from saveFile import listChangeUTF

url = "http://www.datashanghai.gov.cn/query!"
def getInfo(pageUrl):
    html = getHtml(url + pageUrl).decode('utf-8')
    reg = r'<td>\s*(\w*)\r*\s*</td>'
    p = re.compile(reg)
    result = re.findall(p,html)
    return result

#with open("shanghaiProduct.pkl", 'rb') as f:
#    bb = pickle.load(f)

#for each in bb[:10]:
#    print(getInfo(each))
#for each in bb[:10]:
#    print(each)
#with open("shanghaiProduct.cvs", 'w') as f:
#    for each in bb:
#        f.write(each + ",")

#进行正则表达式的检验
"""s = '<a id="ess_ctr507_OrganizationsList_DgdData_ctl02_HylName" class="hylName" href="3350.htm" style="color: rgb(83, 83, 83);">中职</a>'
reg = r'class="hylName" href="(.*)" s.*>([\u4e00-\u9fa5]*)</a>'
p = re.compile(reg)
result = re.findall(p, s)
print(result)"""

with open('egg2.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
    l = ['数据条目','资源分类','关键字','国家分类','部门分类','时间','提供单位','提供地址']
    spamwriter.writerow(l)
    spamwriter.writerow(l)

#if __name__ == '__main__':
    
