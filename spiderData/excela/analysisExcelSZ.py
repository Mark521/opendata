# -*- coding: utf-8 -*-
import xlwt
import xlrd
from dataClass import *
import csv
import time

#数据结构
#城市数据
#------各机构数据
#--------------匹配到的数据、未匹配到的数据、对应的机构
#------城市特有数据

#通过城市数据、城市匹配数据、特征城市机构、机构索引、数据索引(指示机构名称所在位置)
def getExcelData(cityData, cityMatch, jgMap, mapPos, dataPos):
        match = {}
        city = {}   
        size = 0
        citynospecial = []
        same = []
        for each in cityData:
                if each in cityMatch:
                        same.append(each)
        for each in same:
                if each in cityData:
                        cityData.remove(each)
                print('remove成功')
        
        for e in jgMap:
                dictemp = {}
                #获取想对应城市的机构列表
                jgtt = [ ' ' + x[mapPos] for x in jgMap[e]]
                
                #获取匹配到机构的列表
                jgMatch = [x for x in cityMatch if x[2] == e]
                jgTest = list(set([x[6] for x in jgMatch]))
                #获取对应城市机构未匹配到的条目
                notMatch = [x for x in cityData if x not in jgMatch]
                jgNotMatch = [x for x in notMatch if x[dataPos] in jgtt]
                #jgNotMatch = [x for x in notMatch if x[dataPos] in jgTest]

                
                #将匹配到的数据, 未匹配条目和机构存储
                dictemp['match'] = jgMatch
                dictemp['notmatch'] = jgNotMatch
                dictemp['jg'] = jgtt
                #dictemp['jg'] = jgTest
                
                #存储匹配数据
                citynospecial.extend(jgMatch)
                citynospecial.extend(jgNotMatch)
                print(e, jgtt , end = '')
                #print(e, jgTest , end = '')
                print(len(jgMatch), len(jgNotMatch))
                
                #将对应机构数据存储到总字典中
                match[e] = dictemp
        special = [x for x in cityData if x not in citynospecial]
        special.sort(key = lambda x:x[dataPos]) 
        city['city'] = match
        city['special'] = special
        return city

#获取一组数据按照机构字典
def getDataFromResource(data, pos):
        jg = list(set([e[pos] for e in data if e[0] != '']))
        dataDict = {}
        for e in jg:
                jgdata = [x for x in data if x[pos] == e]
                dataDict[e] = jgdata
        return dataDict


#设置单元格颜色                       
def setColor(i):
        stylei = xlwt.XFStyle()
        patterni= xlwt.Pattern()          #为样式创建图案
        patterni.pattern=1                #设置底纹的图案索引，1为实心，2为50%灰色，对应为excel文件单元格格式中填充中的图案样式
        patterni.pattern_fore_colour=i    #设置底纹的前景色，对应为excel文件单元格格式中填充中的背景色
        patterni.pattern_back_colour=35   #设置底纹的背景色，对应为excel文件单元格格式中填充中的图案颜色
        stylei.pattern=patterni
        return stylei

#保存到XSL文件中
def saveAsXSLFile(data, city, sheetname, fileName):

        table=fileName.add_sheet(sheetname,cell_overwrite_ok=True)
        index = 0
        index_city = {}
        index_city['bj'] = [1,2,3,4,5,6,11,12,13]
        index_city['sh'] = [1,2,3,4,5,6,14,15,16]
        index_city['wh'] = [0,1,2,3,4,5,6]
        pos = index_city[city]
        red = setColor(2)
        wihte = setColor(1)
        green = setColor(3)
        gray = setColor(23)
        yellow = setColor(5)
        for e in data['city']:
                table.write(index,0,e,red)         #使用样式
                table.write(index,1,','.join(data['city'][e]['jg']), wihte)
                table.write(index, 2, str(len(data['city'][e]['match'])), wihte)
                table.write(index, 3,  str(len(data['city'][e]['notmatch'])), wihte)
                index += 1
                for d in range(len(data['city'][e]['match'])):
                        temp = data['city'][e]['match'][d]
                        for cell in range(len(pos)):
                                table.write(index, cell+1, data['city'][e]['match'][d][pos[cell]], green)
                        index += 1
                for d in range(len(data['city'][e]['notmatch'])):
                        temp = data['city'][e]['notmatch'][d]
                        
                        for cell in range(len(pos)):
                                table.write(index, cell+1, data['city'][e]['notmatch'][d][pos[cell]], gray)
                        index += 1
        table.write(index, 0, city + '特有', red)
        index += 1
        ddd = {}
        ddd['bj']=  [11,12,13]
        ddd['sh'] = [14,15,16]
        ddd['wh'] = [4,5,6]
        for d in range(len(data['special'])):
                
                temp = data['special'][d]
                for cell in range(len(ddd[city])):
                        table.write(index, cell+1, data['special'][d][ddd[city][cell]], yellow)
                index += 1

def setList(data):
        news = []
        for d in data:
            if d not in news:
                news.append(id)
        return news


xls = xlrd.open_workbook('基础对比表.xlsx')
wuhan = xlrd.open_workbook('深圳武汉数据对比20160706.xlsx')
entry = wuhan.sheets()[0]
mapped = xls.sheets()[1]
#excel表数据条目信息
data = [entry.row_values(e) for e in range(2, entry.nrows)]
#机构映射信息
mapList = [mapped.row_values(e) for e in range(1, mapped.nrows)]

#深圳机构信息
szdata = [e for e in data if e[0] != '']
jg = list(set([e[2] for e in data if e[0] != '']))
jgMapped = {}
for e in jg:
        same = [x for x in mapList if x[1] == e]
        jgMapped[e] = same
#获得北京机构上海机构武汉机构信息


#北京和上海各自匹配到的数据

whdata = [x for x in data if x[4] != '']
whmatch = [x for x in data if x[0] != '' and x[4] != '']



file = xlwt.Workbook()

whMatch = getExcelData(whdata, whmatch, jgMapped, 2, 6)


#whMatch['city'] = sorted(whMatch['city'].items(), key = lambda d:len(d[1]['notmatch']) + len(d[1]['match']))

saveAsXSLFile(whMatch, 'wh', '武汉-深圳', file)

timestr = str(time.strftime("%Y%m%d", time.localtime()))

file.save(timestr +'武汉数据对比.xls')
"""file = xlwt.Workbook()
table=file.add_sheet('aaa name',cell_overwrite_ok=True)
index = 0

a = setColor(1)
b = setColor(3)
c = setColor(23)
for e in bjjgMatch['city']:
        table.write(index,0,e,setColor(2))         #使用样式
        table.write(index,1,','.join(bjjgMatch['city'][e]['jg']), a)
        table.write(index, 2, str(len(bjjgMatch['city'][e]['match'])), a)
        table.write(index, 3,  str(len(bjjgMatch['city'][e]['notmatch'])), a)
        index += 1
        for d in range(len(bjjgMatch['city'][e]['match'])):
                for cell in range(len(bjjgMatch['city'][e]['match'][d])):
                        table.write(index, cell+1, bjjgMatch['city'][e]['match'][d][cell], b)
                index += 1
        for d in range(len(bjjgMatch['city'][e]['notmatch'])):
                for cell in range(len(bjjgMatch['city'][e]['notmatch'][d])):
                        table.write(index, cell+1, bjjgMatch['city'][e]['notmatch'][d][cell], c)
                index += 1
        print(e)
for d in range(len(bjjgMatch['special'])):
        for cell in range(len(bjjgMatch['special'][d])):
                table.write(index, cell+1, bjjgMatch['special'][d][cell], c)
        index += 1"""

#新建一个excel文件
#file=xlwt.Workbook()
#新建一个sheet
#table=file.add_sheet('sheet name',cell_overwrite_ok=True)
#for i in range(0,256):
#        stylei= xlwt.XFStyle()            #初始化样式
#        patterni= xlwt.Pattern()          #为样式创建图案
#        patterni.pattern=1                #设置底纹的图案索引，1为实心，2为50%灰色，对                                            应为excel文件单元格格式中填充中的图案样式
#        patterni.pattern_fore_colour=i    #设置底纹的前景色，对应为excel文件单元格格式                                            中填充中的背景色
#        patterni.pattern_back_colour=35   #设置底纹的背景色，对应为excel文件单元格格式                                            中填充中的图案颜色
#        stylei.pattern=patterni           #为样式设置图案
#        table.write(i,0,i,stylei)         #使用样式

#file.save('bj.xls')
