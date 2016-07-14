
#coding=utf-8

import csv
import pickle

#with open('egg2.csv', 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow([1,4,3,23,2,4,2])
#    spamwriter.writerow([1,243,43,2,4,5,3])、

def saveAsCSV(listTemp, fileName):
    title = ['数据条目','资源分类','关键字','国家分类','部门分类','时间','提供单位','提供地址']
    listTemp.insert(0, title)
    with open(fileName + '.csv', 'w') as csvfile:
        for each in listTemp:
            listS = changePoint(each)
            csvfile.write(listS)
            csvfile.write('\n')
        csvfile.write('\n')

def saveAsPKL(listTemp, fileName):
    with open(fileName + '.pkl', 'wb') as pklfile:
        pickle.dump(listTemp, pklfile)

def readFromPKL(fileName):
    with open(fileName + '.pkl', 'rb') as pklfile:
        listTemp = pickle.load(pklfile)
    return listTemp

def listChangeUTF(listTemp):
    l = []
    for each in listTemp:
        each = each.encode('UTF-8')
        l.append(each)

    return l

def changePoint(listTemp):
    listS = []
    for each in listTemp:
        listS.append(each.replace(',', '、'))
    listS = str(listS)[1:-1]
    listS = listS.replace('\'', '')
    listS = listS.replace('[', '')
    listS = listS.replace(']', '')
    return listS
