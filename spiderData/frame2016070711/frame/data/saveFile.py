
#coding=utf-8

import csv
import pickle

#with open('egg2.csv', 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow([1,4,3,23,2,4,2])
#    spamwriter.writerow([1,243,43,2,4,5,3])、


def readFromPKL(fileName):
    with open(fileName + '.pkl', 'rb') as pklfile:
        listTemp = pickle.load(pklfile)
    return listTemp

a = readFromPKL('BJEntry')

b = readFromPKL('SHEntry')

c = readFromPKL('WHEntry')
