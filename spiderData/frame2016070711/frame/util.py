import datetime
import os
import glob

#根据时间差返回当前时间的第几天
def perDayTime(d):
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(d)
    return yes_time


def files(curr_dir = '.', ext = '*.pkl'):
    """当前目录下的文件"""
    for i in glob.glob(os.path.join(curr_dir, ext)):
        yield i
        
def fileCheck(filename = '', suffix= 'pkl'):
    flag = True
    fileList = []
    for e in files('.', ext = '*' + filename + '*.' + suffix):
        e = e.replace('\\', '')
        fileList.append(e[1:])
    if len(fileList) > 0:
        message =  'OK, "%s" file exists'
    else:
        message = 'Sorry, "%s" file not exists'
        flag = False
    print(message%(filename))
    return flag, fileList

    
