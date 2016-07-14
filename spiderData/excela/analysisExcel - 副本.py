# -*- coding: utf-8 -*-
import xlwt
import xlrd
from dataClass import *
import csv

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

#file.save('colour.xls')


def getExcelData():
                





xls = xlrd.open_workbook('基础对比表.xlsx')
entry = xls.sheets()[0]
mapped = xls.sheets()[1]
#excel表数据条目信息
data = [entry.row_values(e) for e in range(2, entry.nrows)]
#机构映射信息
mapList = [mapped.row_values(e) for e in range(1, mapped.nrows)]

#深圳机构信息
jg = list(set([e[2] for e in data if e[0] != '']))
jgMapped = {}
for e in jg:
        same = [x for x in mapList if x[1] == e]
        jgMapped[e] = same
#获得北京机构上海机构武汉机构信息


#北京和上海各自匹配到的数据
dd = []
with open('北京市数据条目.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
                dd.append(line)
bjdata = [x for x in data if x[11] != '']
listbjdata = bjdata
bjdata = []
for e in listbjdata:
        temp = e
        for a in dd:
                if len(a)==3 and temp[13] == a[0]:
                        temp[12] = a[2]
        bjdata.append(temp)

bjmatch = [x for x in data if x[0] != '' and x[11] != '']
shdata = [x for x in data if x[14] != '']
shmatch = [x for x in data if x[0] != '' and x[14] != '']

bjjgMatch = {}
size = 0
bjnospecial = []
for e in jgMapped:
	print(e, end = '\t')
	dictemp = {}
	bjjg = [x[3] for x in jgMapped[e]]
	#进行数据分类
	#匹配到的机构数据
	jgMatch = [x for x in bjmatch if x[2] == e]
	#没有匹配到的机构数据
	jgNotMatch = [x for x in bjdata if x[12] in bjjg and  x not in jgMatch]
        #城市特有的数据
	dictemp['match'] = jgMatch
	dictemp['notmatch'] = jgNotMatch
	dictemp['bjjg'] = bjjg
	bjnospecial.extend(jgMatch)
	bjnospecial.extend(jgNotMatch)
	print(len(jgMatch), len(jgNotMatch), bjjg)
	size = size  + len(jgMatch)+ len(jgNotMatch)
	bjjgMatch[e] = dictemp
	#for each in jgMatch:
		#print(each[2], each[3], each[11], each[13])

special = [x for x in bjdata if x not in bjnospecial]
special.sort(key=lambda x:x[12])
bjjgMatch['special'] = special

