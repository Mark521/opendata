from downloadBJData import *
from downloadSHData import *
from downloadWHData import *
from analysisData import *


from saveFile import *
filenameBJ = './data/BJEntry'
filenameWH = './data/WHEntry'
filenameSH = './data/SHEntry'


import time
'''
当前文件为实现下载北京、武汉、上海数据的函数
以及对匹配的数据准备
'''


todayTime = time.strftime('%Y%m%d', time.localtime())
#下载背景数据
def downBJ(window):

    window.systemPrint('开始下载北京数据')
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
        temp = getBJPageLinked(ajgUrl + each[0], each[1])
        if(int(each[2])> 20):
            tempUrl = ''
            tempUrl = '' + ajgUrl + each[0]
            tempss = tempUrl[:-4] + '1.htm'
            temp.extend(getBJPageLinked(tempss, each[1]))
        window.systemPrint(str(len(temp)) + each[1])
        infoList.extend(temp)

    #将所有信息保存到类中
    classList = []
    for each in infoList:
        temp = Data(each[2],each[1], each[0], 'BJ')
        classList.append(temp)
    window.systemPrint('数据分析中...')
    saveAsPKL(classList, './data/BJEntry')
    window.systemPrint('数据保存成功')


#下载上海的数据信息
def downSH(window):

    window.systemPrint('开始下载上海数据')
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
    productLinkedList = getSHAllLinked(productPageUrl, "数据", window)
    appLinkedList = getSHAllLinked(appPageUrl, "应用", window)
    interfaceLinkedList = getSHAllLinked(interfacePageUrl, "接口", window)

    window.systemPrint('开始抓取数据')
    length = (len(productLinkedList) + len(appLinkedList) + len(interfaceLinkedList))/20
    sign = 0
    ll = []
    for each in interfaceLinkedList:
        window.systemPrint('|')
        ll.append(getSHInfo(each[0], each[3], each[1]))
    for each in productLinkedList:
        window.systemPrint('|')
        ll.append(getSHInfo(each[0], each[3], each[1]))
    for each in appLinkedList:
        ll.append(getSHInfo(each[0], each[3], each[1]))
        window.systemPrint('|')
    #saveAsCSV(ll, "上海应用开放")
    window.systemPrint('抓取数据成功')
    classList = []
    for each in ll:
        temp = Data(each[2],each[1], each[0], 'SH')
        classList.append(temp)
    window.systemPrint('数据分析中...')
    saveAsPKL(classList, './data/SHEntry')
    window.systemPrint('数据保存成功')


#下载武汉数据信息
def downWH(window):

    window.systemPrint('开始下载武汉数据')
    #武汉数据开放列表的总页面
    listUrl = 'http://www.wuhandata.gov.cn/whdata/resources_listPage.action'
    infoUrl = 'http://www.wuhandata.gov.cn/whdata/resources_list.action?category=25bde262-31b4-4901-8d53-527631005f6a&pageNum='
    
    #获取数据开放的条目,包括开放机构和开放项目
    orgResult, resResult = getResourceId(listUrl)

    #用于存储各个数据开放的条目
    dataList = []

    #对数据也进行循环读取
    page = 1
    dataInfo = getWHAllPageLinked(infoUrl + str(page))
    totlePage = dataInfo['pages']
    dataList.extend(getWHInfoFromJson(dataInfo['list']))
    while(dataInfo['hasNextPage'] == True):
        page = page + 1
        window.systemPrint('共'+str(totlePage)+'页,当天正在下载第' +str(page) + "页" )
        dataInfo = getWHAllPageLinked(infoUrl + str(page))
        dataList.extend(getWHInfoFromJson(dataInfo['list']))

    #将所有信息保存到类中
    classList = []
    for each in dataList:
        temp = Data(each[3],each[2], each[0], 'WH')
        classList.append(temp)
    window.systemPrint('数据分析中...')
    saveAsPKL(classList, './data/WHEntry')
    window.systemPrint('数据保存成功')
    
def matchL(window,city):
    #加载类数据,为关键字检索做准备
    window.systemPrint('加载数据中...')
    dataBJ = readFromPKL(filenameBJ)
    dataWH = readFromPKL(filenameWH)
    dataSH = readFromPKL(filenameSH)
    
    #对加载数据进行初始化
    entryBJ = initEntryFromData(dataBJ)
    entryWH = initEntryFromData(dataWH)
    entrySH = initEntryFromData(dataSH)
    time.sleep(0.1)
    window.systemPrint('加载数据完成')
    time.sleep(0.1)

    if city == 'sh':
        return entryBJ, entrySH
    elif city == 'bj':
        return entryBJ, entryBJ
    elif city == 'wh':
        return entryBJ, entryWH
    else:
        return 0
