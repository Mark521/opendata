# -*- coding: cp936 -*-
from tkinter import *
import os
from tkinter.messagebox import *
import time

#导入进行数据操作的方法和类
from downloadBJData import *
from saveFile import *
from analysisData import *



filenameBJ = 'BJEntry'
filenameWH = 'WHEntry'
filenameSH = 'SHEntry'

class Window:

    data = []
    index_data = 0
    other = []
    index_other = 0
    same_data = []
    index_same_data = 0
    diff_data = []
    index_diff_data = 0
    
    def __init__(self, title='数据开放条目校验', width=600, height=500, staFunc=bool, stoFunc=bool):
        self.w = width
        self.h = height
        self.stat = True
        self.staFunc = staFunc
        self.stoFunc = stoFunc
        self.staIco = None
        self.stoIco = None
        self.var_R_int = None
        self.root = Tk(className=title)
        self.city = None
        self.lb_int = None

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int( (ws/2) - (self.w/2) )
        y = int( (hs/2) - (self.h/2) )
        #self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def packBtn(self):
        self.frm = Frame(self.root)


        Label(self.root, text='选择数据源',pady = 0, font=('Arial', 15)).grid(sticky=W)
        self.btnWH = Button(self.root,command = lambda:self.selectSource('wh'),text='武汉数据', width=15, height=2)
        self.btnSH = Button(self.root,command = lambda:self.selectSource('sh'),text='上海数据', width=15, height=2)
        self.btnBJ = Button(self.root,command = lambda:self.selectSource('bj'),text='北京数据', width=15, height=2)
        self.btnCL = Button(self.root,text='重置', width=15, height=2)

        self.btnWH.grid(column=0,row=1,sticky=W)
        self.btnSH.grid(column=0,row=2,sticky=W)
        self.btnBJ.grid(column=0,row=3,sticky=W)
        self.btnCL.grid(column=0,row=4,sticky=W)
        self.match = Button(self.root, text = '匹配数据', command=self.matchData, width=15, height=2)

        Label(self.root, text='数据源',bg='red' ,borderwidth=1, font=('Arial', 15), width=15, height=2).grid(column=2,row=0,sticky=W)
        self.source = StringVar()
        self.source.set('未选择')
        Label(self.root,textvariable = self.source, font=('Arial', 15),bg='yellow', width=15, height=2).grid(column=3,row=0,sticky=W)
        self.lb_int = Text(self.root,bg='red', font =('Verdana',12), width=40)#, width=65, height=20
        #self.lb_int.bind('<Button-1>', self.get_int,)
        self.scrl_int = Scrollbar(self.root)
        self.scrl_int.grid(column=7, row = 1, rowspan=5,sticky=E)
        self.lb_int.configure(yscrollcommand = self.scrl_int.set)
        self.lb_int.grid(column=1,row=1,columnspan=4, rowspan=5,sticky=E)
        self.scrl_int['command'] = self.lb_int.yview
        self.match.grid(column=5,row=0,sticky=W)
        self.loaddata = Button(self.root, text='读取数据',command=self.downloaddata, width=15, height=2)
        self.loaddata.grid(column=4,row=0,sticky=W)
       
    

    #进行数据初始化
    def downloaddata(self):
        if self.city == None:
            showinfo(title='提示信息',message='还未选择数据源')
        else:
            pass
            #downddd(self)
        '''elif self.lb_int == None:
            #显示当前的进程
            
            #设置当前窗口不能进行其他操作
            self.stat = False
        else:
            showinfo(title='提示信息',message='正在进行数据分析')
            self.lb_int.destroy()
            self.scrl_int.destroy()
            self.match.destroy()
            self.lb_int = None
            self.city = None
            self.match = None
            self.source.set('未选择')
            self.stat = True'''

    #进行数据匹配界面的初始化和数据的提取
    def matchData(self):

        self.top = Toplevel()
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int( (ws/2) - (self.w/2) )
        y = int( (hs/2) - (self.h/2) )
        self.top.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))
        #数据匹配界面
        Label(self.top, text='数据条目', font=('Arial', 15)).grid(column=2, row=1, sticky=(N, E))
        Label(self.top, text='数据来源', font=('Arial', 15)).grid(column=3, row=1, sticky=(N, E))
        Label(self.top, text='提供机构', font=('Arial', 15)).grid(column=4, row=1, sticky=(N, E))
        Label(self.top, text='深圳条目', font=('Arial', 15)).grid(column=1, row=2, sticky=(N, E))
        Label(self.top, text='武汉条目', font=('Arial', 15)).grid(column=1, row=3, sticky=(N, E))
        Button(self.top, text = '上一条',command=self.pre_topData).grid(column=1, row=4, sticky=(N, E))
        check = PhotoImage(file = 'check.png')
        error = PhotoImage(file = 'error.png')
        Button(self.top, image = check,command=self.bingoData, width=30, height=30).grid(column=2, row=4, sticky=(N, E))
        Button(self.top, image = error,command=self.errorData, width=30, height=30).grid(column=3, row=4, sticky=(N, E))
        #Label(self.top_frm_B, text='数据条目5',bitmap=bm).pack(side=LEFT)
        Button(self.top, text = '下一条',command=self.next_topData).grid(column=4, row=4, sticky=(N, E))

        self.top_str_22 = StringVar()
        #self.top_str_22.set('未设置')
        Label(self.top, textvariable=self.top_str_22, font=('Arial', 15)).grid(column=2, row=2, sticky=(N, E))
        self.top_str_23 = StringVar()
        #self.top_str_23.set('未设置')
        #Label(self.top, textvariable=self.top_str_23, font=('Arial', 15)).grid(column=3, row=2, sticky=(N, E))
        self.top_str_24 = StringVar()
        #self.top_str_24.set('未设置')
        Label(self.top, textvariable=self.top_str_24, font=('Arial', 15)).grid(column=4, row=2, sticky=(N, E))
        self.top_str_32 = StringVar()
       # self.top_str_32.set('未设置')
        Label(self.top, textvariable=self.top_str_32, font=('Arial', 15)).grid(column=2, row=3, sticky=(N, E))
        self.top_str_33 = StringVar()
        #self.top_str_33.set('未设置')
        Label(self.top, textvariable=self.top_str_33, font=('Arial', 15)).grid(column=3, row=3, sticky=(N, E))
        self.top_str_34 = StringVar()
        #self.top_str_34.set('未设置')
        Label(self.top, textvariable=self.top_str_34, font=('Arial', 15)).grid(column=4, row=3, sticky=(N, E))
        self.data, self.other = matchL(self)
        self.data, self.other  = matchList(self.data, self.other)
        self.index_data = 1
        self.top_str_22.set(self.data[0].name)
        self.top_str_23.set(self.data[0].dataType)
        self.top_str_24.set(self.data[0].source)
        self.top_str_32.set(self.other[0].name)
        self.top_str_33.set(self.other[0].dataType)
        self.top_str_34.set(self.other[0].source)
        print(len(self.data))
        for child in self.top.winfo_children():
            child.grid_configure(padx=20, pady=20)
        self.top.mainloop()

    def bingoData(self):
        temp = []
        temp.insert(0, self.data[self.index_data])
        temp.insert(1, self.other[self.index_data])
        if temp in self.diff_data:
            self.diff_data.remove(temp)
            print('从不同删除')
        if temp not in self.same_data:
            self.same_data.append(temp)
            print('从相同添加')
        self.next_topData()
            
    def errorData(self):
        temp = []
        temp.insert(0, self.data[self.index_data])
        temp.insert(1, self.other[self.index_data])
        if temp not in self.diff_data:
            self.diff_data.append(temp)
            print('从不同添加')
        if temp in self.same_data:
            self.same_data.remove(temp)
            print('从相同删除')
        self.next_topData()
    
    def next_topData(self):
        if self.index_data < len(self.data)-1:
            self.top_str_22.set(self.data[self.index_data].name)
            self.top_str_23.set(self.data[self.index_data].dataType)
            self.top_str_24.set(self.data[self.index_data].source)
            self.top_str_32.set(self.other[self.index_data].name)
            self.top_str_33.set(self.other[self.index_data].dataType)
            self.top_str_34.set(self.other[self.index_data].source)
            self.index_data +=1
        else:
            showinfo(title='提示信息',message='完成匹配')
            self.top.destroy()
    def pre_topData(self):
        if self.index_data < len(self.data)-1:
            self.top_str_22.set(self.data[self.index_data].name)
            self.top_str_23.set(self.data[self.index_data].dataType)
            self.top_str_24.set(self.data[self.index_data].source)
            self.top_str_32.set(self.other[self.index_data].name)
            self.top_str_33.set(self.other[self.index_data].dataType)
            self.top_str_34.set(self.other[self.index_data].source)
            self.index_data -=1
        if self.index_data == 0:
            showinfo(title='提示信息',message='已经是第一条数据')
            self.top.destroy()
    def selectSource(self, city):
        
        if self.stat == True:
            s = ''
            self.city = city
            if city == 'sh':
                s = '上海数据'
            if city == 'bj':
                s = '北京数据'
            if city == 'wh':
                s = '武汉数据'
            self.source.set(s)
        else:
            showinfo(title='提示信息',message='正在进行数据分析...')
             
    def event(self):
        self.btnSer['state'] = 'disabled'
        if self.stat:
            self.btnSer['text'] = '启动服务'
            self.stat = False
            self.root.iconbitmap(self.stoIco)
        else:
            self.btnSer['text'] = '停止服务'
            self.stat = True
            self.root.iconbitmap(self.staIco)
        self.btnSer['state'] = 'active'
    def systemPrint(self, s):
        self.lb_int.insert(END, s + '\n')
        time.sleep(0.1)
        self.lb_int.update()
    
    def loop(self):
        #self.root.resizable(False, False)   #禁止修改窗口大小
        self.packBtn()
        self.center()                       #窗口居中
        #self.event()
        self.root.mainloop()
#####################################################################################
def downddd(window):
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
        temp = getPageLinked(ajgUrl + each[0], each[1])
        if(int(each[2])> 20):
            tempUrl = ''
            tempUrl = '' + ajgUrl + each[0]
            tempss = tempUrl[:-4] + '1.htm'
            temp.extend(getPageLinked(tempss, each[1]))
        window.systemPrint(str(len(temp)) + each[1])
        infoList.extend(temp)

    #将所有信息保存到类中
    classList = []
    for each in infoList:
        temp = Data(each[2],each[1], each[0], 'BJ')
        classList.append(temp)
    window.systemPrint('数据分析中...')
    saveAsPKL(classList, 'BJEntry')
    window.systemPrint('数据保存成功')

def matchL(window):
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
    return entryBJ, entrySH

if __name__ == '__main__':
    w = Window(staFunc=bool, stoFunc=bool)
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()
