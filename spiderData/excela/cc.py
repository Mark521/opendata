from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.messagebox import *
import os
import glob
import datetime
import xlrd
import xlwt
from analysisExcel import *


#获取时间字符串
def getTimeStr(sign):
  now_time = datetime.datetime.now()
  if sign == 1:
    return now_time.strftime("%Y%m%d")
  elif sign == 2:
    return now_time.strftime("%Y%m%d%H")
  elif sign == 3:
    return now_time.strftime("%Y%m%H%M")
  else:
    return now_time.strftime("%Y%m%H%M%S")

#打开文件
def choseFile():
  fname = askopenfilename(filetypes=(("表格 files", "*.xls;*.xlsx"),("All files", "*.*") ))
  #print(fname, type(fname))
  if isRightFile(fname):
    showinfo(title='提示信息',message='读取文件成功')
    #showinfo(title='提示信息',message= '保存到文件：' + filename)
    return fname
  else:
    showinfo(title='提示信息',message= '文件读取失败，请检查文件内容')
    return False

#保存文件
def saveAnaLyFile():

  fname = choseFile()
  if fname == False:
    return 0
  filename = ''
  for i in range(1,4):
    filename = getTimeStr(i)
    if filenameCheck(filename):
      break
  print(filename)
  #return filename
  filename = filename + '数据对比.xls'
  xls = xlrd.open_workbook(fname)
  wuhan = xlrd.open_workbook('深圳武汉数据对比20160706.xlsx')
  wuhanEntry = wuhan.sheets()[0]
  entry = xls.sheet_by_name('深圳开放目录汇总')
  mapped = xls.sheet_by_name('部门映射表')
  #excel表数据条目信息
  data = [entry.row_values(e) for e in range(2, entry.nrows)]
  wuhandata = [wuhanEntry.row_values(e) for e in range(2, wuhanEntry.nrows)]
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
  #武汉数据获取
  whdata = [x for x in wuhandata if x[4] != '']
  whmatch = [x for x in wuhandata if x[0] != '' and x[4] != '']
  #北京和上海各自匹配到的数据
  #处理北京数据
  dd = []
  with open('北京市数据条目.csv', 'r') as f:
          reader = csv.reader(f)
          for line in reader:
                  dd.append(line)
  listbjdata = [x for x in data if x[12] != '']
  bjdata = []
  for e in listbjdata:
          temp = e
          for a in dd:
                  if len(a)==3 and temp[13] == a[0]:
                          temp[12] = a[2]
          bjdata.append(temp)
  bjmatch = [x for x in data if x[0] != '' and x[12] != '']
  #处理上海数据
  shdata = [x for x in data if x[15] != '']
  shmatch = [x for x in data if x[0] != '' and x[15] != '']
  #处理深圳特有数据
  leftdata = [x for x in szdata if x not in bjmatch and x not in shmatch]
  wuname = [x[3] for x in whmatch]
  leftdata = [x for x in leftdata if x[3] not in wuname ]
  szleft = getDataFromResource(leftdata, 2)


  #进行文件写入
  file = xlwt.Workbook()
  whMatch = getExcelData(whdata, whmatch, jgMapped, 2, 6)
  saveAsXSLFile(whMatch, 'wh', '武汉-深圳', file)
  bjjgMatch = getExcelData(bjdata, bjmatch,jgMapped, 3, 12 )
  saveAsXSLFile(bjjgMatch, 'bj','北京-深圳', file)
  shjgMatch = getExcelData(shdata, shmatch,jgMapped, 0, 15 )
  saveAsXSLFile(shjgMatch, 'sh','上海-深圳', file)

  table = file.add_sheet('深圳特有数据', cell_overwrite_ok=True)
  index = 0
  for e in szleft:
          table.write(index, 0, e)
          index += 1
          for d in range(len(szleft[e])):
                  for cell in range(len(szleft[e][d][:10])):
                          table.write(index, cell+1, szleft[e][d][cell])
                  index += 1


  timestr = str(time.strftime("%Y%m%d", time.localtime()))

  file.save(filename)
  showinfo(title='提示信息',message='保存至' + filename)


  root.destroy()

  
#检查当前文件是否有重名
def filenameCheck(filename):
  curr_dir = '.'
  ext = filename + '*.xls'
  fileList = []
  for i in glob.glob(os.path.join(curr_dir, ext)):
    fileList.append(i)
  if len(fileList) > 0:
    return False
  else:
    return True
    


#判断文件格式是否正确
def isRightFile(fname):
  
  if fname == '':
  #  showinfo(title='提示信息',message='未选择任何文件')
    return False
  else:
    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_names()
    flag = '深圳开放目录汇总' in sheet and '部门映射表' in sheet
    #print(sheet)
    return flag



if __name__ == '__main__':
  fname = ''
  filename = ''
  root = Tk(className='表格数据合并')
  ws = root.winfo_screenwidth()
  hs = root.winfo_screenheight()
  root.geometry('250x100+{}+{}'.format(int(ws/2 - 125), int(hs/2 - 50)))
  Button(root, command=saveAnaLyFile, text='分析文件', font=('Arial', 15), width=15, height=2,anchor='center').place(relx=0.15, rely=0.2)

  root.mainloop()
