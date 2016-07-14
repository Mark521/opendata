# -*- coding: cp936 -*-
from tkinter import *
import os
from tkinter.messagebox import *
import time
from logtext import *

#导入进行数据操作的方法和类

from downcity import *
from saveFile import *
from analysisData import *
import time


filenameBJ = './data/BJEntry'
filenameWH = './data/WHEntry'
filenameSH = './data/SHEntry'


todayTime = time.strftime('%Y%m%d%H%m', time.localtime())


class Window:

    data = []
    index_data = 0
    other = []
    index_other = 0
    same_data = []
    index_same_data = 0
    diff_data = []
    index_diff_data = 0

    lineNum = 0
    
    def __init__(self, title='数据开放条目校验', width=500, height=300):
        self.w = width
        self.h = height
        self.stat = True
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
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def packBtn(self):
        self.frm = Frame(self.root)

        lineLen = 0.2
        Label(self.root, text='选择数据源',pady = 0, font=('Arial', 15)).place(rely = lineLen*0, relheight = lineLen, relwidth = lineLen)
        
        self.btnWH = Button(self.root,command = lambda:self.selectSource('wh'),text='武汉数据', font=('Arial', 15), width=15, height=2)
        self.btnSH = Button(self.root,command = lambda:self.selectSource('sh'),text='上海数据', font=('Arial', 15), width=15, height=2)
        self.btnBJ = Button(self.root,command = lambda:self.selectSource('bj'),text='北京数据', font=('Arial', 15), width=15, height=2)
        self.btnCL = Button(self.root,text='重置', width=15, height=2)

        self.btnWH.place(rely = lineLen*1, relheight = lineLen, relwidth = lineLen)
        self.btnSH.place(rely = lineLen*2, relheight = lineLen, relwidth = lineLen)
        self.btnBJ.place(rely = lineLen*3, relheight = lineLen, relwidth = lineLen)

        Label(self.root, text='数据源',bg='red' ,borderwidth=1, font=('Arial', 15), width=15, height=2).place(relx = lineLen, relwidth = lineLen, relheight = lineLen)
        self.source = StringVar()
        self.source.set('未选择')
        Label(self.root,textvariable = self.source, font=('Arial', 15),bg='yellow', width=15, height=2).place(relx = lineLen*2, relwidth = lineLen, relheight = lineLen)
        self.lb_int = Text(self.root, font =('Verdana',12), width=40)#, width=65, height=20
        #self.lb_int.bind('<Button-1>', self.get_int,)
        self.scrl_int = Scrollbar(self.root)
        self.scrl_int.place(relx = 1- 0.04,rely = lineLen, relwidth = 0.04, relheight = 0.8)
        self.lb_int.configure(yscrollcommand = self.scrl_int.set)
        self.lb_int.place(relx = lineLen, rely = lineLen,relwidth = 1 - lineLen - 0.04, relheight = 1 - lineLen)
        self.scrl_int['command'] = self.lb_int.yview

        self.match = Button(self.root, text = '匹配数据', font=('Arial', 15), command=self.matchData)
        self.match.place(relx = lineLen*4, relwidth = lineLen, relheight = lineLen)
        
        self.loaddata = Button(self.root, text='读取数据', font=('Arial', 15),command=self.downloaddata)
        self.loaddata.place(relx = lineLen*3, relwidth = lineLen, relheight = lineLen)
       
    #进行数据初始化
    def downloaddata(self):
        if self.city == None:
            showinfo(title='提示信息',message='还未选择数据源')
        elif self.city == 'bj':
            downBJ(self)
        elif self.city == 'sh':
            downSH(self)
        elif self.city == 'wh':
            downWH(self)
        else:
            showinfo(title='提示信息',message='不是北京数据')

    #进行数据匹配界面的初始化和数据的提取
    def matchData(self):
        self.same_data = []
        self.diff_data = []
        self.data, self.other = matchL(self, self.city)
        self.data, self.other  = matchList(self.data, self.other)

        self.top = Toplevel()
        self.top.resizable(False, False)
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int( (ws/2) - (400) )
        y = int( (hs/2) - (150) )
        self.top.geometry('{}x{}+{}+{}'.format(800, 300, x, y))
        #数据匹配界面
        linx = 0.001
        liny = 0.01
        
        xpos = 0.2 + linx
        ypos = 0.2
        xlen = 0.266666
        ylen = 0.3
        #数据属性
        Label(self.top, text='数据条目',font=('Arial', 15),borderwidth = 3,bg='#B8CCE4').place(relx=0.2, relheight=xpos, relwidth=xlen)
        Label(self.top, text='数据来源',font=('Arial', 15),borderwidth = 3).place(relx=0.466666, relheight=xpos, relwidth=xlen)
        Label(self.top, text='提供机构',font=('Arial', 15),borderwidth = 3,bg='#B8CCE4').place(relx=0.73332, relheight=xpos, relwidth=xlen)
        firCity = StringVar()
        firCity.set('深圳条目')
        Label(self.top,textvariable = firCity ,font=('Arial', 15),anchor = 'e',bg='#B8CCE4').place(rely=ypos, relheight=0.3, relwidth=ypos)
        secCity = StringVar()
        secCity.set('武汉条目')
        Label(self.top,textvariable = secCity,font=('Arial', 14),anchor = 'e').place(rely=ypos + ylen, relheight=xpos, relwidth=ypos)

        #提示信息
        self.pageMessage = StringVar()
        Label(self.top, textvariable = self.pageMessage, font=(('Arial', 12)),anchor='e').place(rely=ypos + 2*ylen, relheight=xpos, relwidth=ypos + 0.1)

        #进行判断按钮
        check = PhotoImage(file = 'check.png')
        error = PhotoImage(file = 'error.png')
        Button(self.top, image = check,command=self.bingoData).place(relx = 0.5-0.08 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.08)
        Button(self.top, image = error,command=self.errorData).place(relx = 0.5 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.08)

        #上一条下一条按钮
        Button(self.top, text = '上一条',command=self.pre_topData, width=30, height=30).place(relx = 0.7 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.1)
        Button(self.top, text = '下一条',command=self.next_topData, width=30, height=30).place(relx = 0.8 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.1)

        #中间属性值
        self.top_str_22 = StringVar()
        Label(self.top,textvariable=self.top_str_22,font=('Arial', 15),wraplength=200).place(rely=ypos,relx=xpos, relheight=ylen, relwidth=xlen)

        self.top_str_23 = StringVar()
        Label(self.top,textvariable=self.top_str_23,font=('Arial', 15),wraplength=200,bg='#B8CCE4').place(rely=ypos,relx=xpos+xlen, relheight=ylen, relwidth=xlen)

        self.top_str_24 = StringVar()
        Label(self.top,textvariable=self.top_str_24,font=('Arial', 15),wraplength=200).place(rely=ypos,relx=xpos+2*xlen, relheight=ylen, relwidth=xlen)

        self.top_str_32 = StringVar()
        Label(self.top,textvariable=self.top_str_32,font=('Arial', 15),wraplength=200,bg='#B8CCE4').place(rely=ypos+ ylen,relx=xpos, relheight=ylen, relwidth=xlen)

        self.top_str_33 = StringVar()
        Label(self.top,textvariable=self.top_str_33,font=('Arial', 15),wraplength=200).place(rely=ypos+ ylen,relx=xpos+xlen, relheight=ylen, relwidth=xlen)

        self.top_str_34 = StringVar()
        Label(self.top,textvariable=self.top_str_34,font=('Arial', 15),wraplength=200,bg='#B8CCE4').place(rely=ypos+ ylen,relx=xpos+2*xlen, relheight=ylen, relwidth=xlen)

        #进行属性初始化
        self.index_data = 0
        self.top_str_22.set(self.data[self.index_data].name)
        self.top_str_23.set(self.data[self.index_data].dataType)
        self.top_str_24.set(self.data[self.index_data].source)
        self.top_str_32.set(self.other[self.index_data].name)
        self.top_str_33.set(self.other[self.index_data].dataType)
        self.top_str_34.set(self.other[self.index_data].source)
        self.pageMessage.set(self.getPageMessage(self.index_data, len(self.data)))

        time.sleep(1.6)
        self.top.mainloop()
    
    def getPageMessage(self, currentPage, totolPage):
        return '当前第'+str(currentPage + 1)+'页,共'+str(totolPage)+ '页'

    #当匹配到相同的数据后进行的操作
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
    #当匹配到不同的数据
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

    #获取下一条数据
    def next_topData(self):
        self.index_data +=1
        if self.index_data < len(self.data):
            
            self.top_str_22.set(self.data[self.index_data].name)
            self.top_str_23.set(self.data[self.index_data].dataType)
            self.top_str_24.set(self.data[self.index_data].source)
            self.top_str_32.set(self.other[self.index_data].name)
            self.top_str_33.set(self.other[self.index_data].dataType)
            self.top_str_34.set(self.other[self.index_data].source)
            self.pageMessage.set(self.getPageMessage(self.index_data, len(self.data)))
        if self.index_data == len(self.data):
            showinfo(title='提示信息',message='完成匹配')
            print(len(self.diff_data))
            for e in self.diff_data:
                print(e[0].name, e[1].name)
            for e in self.same_data:
                print(e[0].name, e[1].name)
            print(len(self.same_data))
            self.top.destroy()
            
    #获取前一条数据
    def pre_topData(self):
        if self.index_data > 0:
            self.index_data -=1
            self.top_str_22.set(self.data[self.index_data].name)
            self.top_str_23.set(self.data[self.index_data].dataType)
            self.top_str_24.set(self.data[self.index_data].source)
            self.top_str_32.set(self.other[self.index_data].name)
            self.top_str_33.set(self.other[self.index_data].dataType)
            self.top_str_34.set(self.other[self.index_data].source)
            
            self.pageMessage.set(self.getPageMessage(self.index_data, len(self.data)))
        if self.index_data == 0:
            showinfo(title='提示信息',message='已经是第一条数据')
            #self.top.destroy()

    #选择数据源
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
    #向当前文本框输出文本
    def systemPrint(self, s):
        col = len(s)
        logging.info(s)
        self.lb_int.insert(END, s + '\n')
        
        time.sleep(0.1)
        self.lb_int.update()
        self.lineNum +=1
        self.lb_int.see(str(float(self.lineNum)))
        
    
    def loop(self):
        self.root.resizable(False, False)   #禁止修改窗口大小

        self.packBtn()
        self.center()                       #窗口居中
        #self.event()
        self.root.mainloop()


#####################################################################################



if __name__ == '__main__':
    initLogging('myapp.log')
    w = Window()
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()

'''#下载背景数据
def downdBJ(window):
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


#下载上海的数据信息
def downloadSH(window):
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
    productLinkedList = getAllLinked(productPageUrl, "数据")
    appLinkedList = getAllLinked(appPageUrl, "应用")
    interfaceLinkedList = getAllLinked(interfacePageUrl, "接口")

    print('开始抓取数据')
    ll = []
    for each in interfaceLinkedList:
        print('|', end = '')
        ll.append(getInfo(each[0], each[3], each[1]))
    for each in productLinkedList:
        print('|', end = '')
        ll.append(getInfo(each[0], each[3], each[1]))
    for each in appLinkedList:
        print('|', end = '')
        ll.append(getInfo(each[0], each[3], each[1]))
    #saveAsCSV(ll, "上海应用开放")
    print('抓取数据成功')
    classList = []
    for each in infoList:
        temp = Data(each[2],each[1], each[0], 'SH')
        classList.append(temp)
    print('数据分析中...')
    saveAsPKL(classList, './data/SHEntry')
    print('数据保存成功')


#下载武汉数据信息
def dowmloadWH(window)
    #武汉数据开放列表的总页面
    listUrl = 'http://www.wuhandata.gov.cn/whdata/resources_listPage.action'
    infoUrl = 'http://www.wuhandata.gov.cn/whdata/resources_list.action?category=25bde262-31b4-4901-8d53-527631005f6a&pageNum='

    #获取数据开放的条目,包括开放机构和开放项目
    orgResult, resResult = getResourceId(listUrl)

    #用于存储各个数据开放的条目
    dataList = []

    #对数据也进行循环读取
    page = 1
    dataInfo = getAllPageLinked(infoUrl + str(page))
    totlePage = dataInfo['pages']
    dataList.extend(getInfoFromJson(dataInfo['list']))
    while(dataInfo['hasNextPage'] == True):
        page = page + 1
        print('共'+str(totlePage)+'页,当天正在下载第' +str(page) + "页" )
        dataInfo = getAllPageLinked(infoUrl + str(page))
        dataList.extend(getInfoFromJson(dataInfo['list']))


    #将所有信息保存到类中
    classList = []
    for each in dataList:
        temp = Data(each[3],each[2], each[0], 'WH')
        classList.append(temp)
    print('数据分析中...')
    saveAsPKL(classList, './data/WHEntry')
    print('数据保存成功')
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
'''
