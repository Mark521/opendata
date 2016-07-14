#coding=utf-8
"""
    代码进行关键字比较,得出每个词与其他城市数据条目的匹配率
"""


from dataClass import EntryData
from dataClass import Data
from saveFile import readFromPKL
import pickle
import re
import jieba
import xlrd

filenameBJ = './data/BJEntry'
filenameWH = './data/WHEntry'
filenameSH = './data/SHEntry'

collection = ['django_migrations.py','django_admin_log.py','main_generator.py','migrations.py','api_user.doc','user_group.doc','accounts.txt']
city = ['上海市公安局','北京市公安局','南京市公安局','天津市公安局','深圳市公安局','重庆市公安局','北京市交警支队']

def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        print(match)
        if match:
            suggestions.append(item)
        else:
            print(u'木有')

    return suggestions

def getpplList(data):
    listTemp = []
    for each in data:
        listTemp.append(each.name)
    strList = ','.join(listTemp)
    listTemp = list(set(jieba.cut(strList)))
    return listTemp

def matchList(entrys1, entrys2):
    match1 = []
    match2 = []
    pos = 0
    for e in entrys1:
        for a in entrys2:
            match , size = e.matchWithEntry(a)
            #if match != 0 and match/size >=0.618:
            if match > 0:
                match1.insert(pos, e)
                match2.insert(pos, a)
                pos +=1
    return match1, match2

def initEntryFromData(data):
    entry = []
    for each in data:
        temp = EntryData()
        temp.setFromData(each)
        entry.append(temp)
    return entry
    
#print(fuzzyfinder('市安', city))

"""if __name__ == '__main__':
    #加载类数据,为关键字检索做准备
    dataBJ = readFromPKL(filenameBJ)
    dataWH = readFromPKL(filenameWH)
    dataSH = readFromPKL(filenameSH)

    #对加载数据进行初始化
    entryBJ = initEntryFromData(dataBJ)
    entryWH = initEntryFromData(dataWH)
    entrySH = initEntryFromData(dataSH)

    #准备每个城市的分词列表
    #listBJ = getpplList(dataBJ)
    #listWH = getpplList(dataWH)
    #listSH = getpplList(dataSH)

    #bjSame = []
    #shSame = []
    #for e in entryBJ:
	#for a in entrySH:
		#matchNum, size = e.matchWithEntry(a)
		#if matchNum != 0 and matchNum/size >0.618:
                        #bjSame.
			#print(e.name, '<-->', a.name, '匹配成功')
    #printMatch
    
    data = xlrd.open_workbook('北京上海对比开放目录-标注后.xlsx')
    shEntry = data.sheets()[0]
    szEntry = data.sheets()[0]
    nrows = szEntry.nrows
    ncols = szEntry.ncols
    szdata = []
    for i in range(nrows):
        temp = EntryData()
        sss = szEntry.row_values(i)
        temp.setFromString(sss[2], '', sss[3], 'SZ')
        szdata.append(temp)
    for e in szdata:
        if e.name == ' ':
            szdata.remove(e)
    for e in szdata:
        if e.name == '':
            szdata.remove(e)
    szdata = szdata[1:392]"""
