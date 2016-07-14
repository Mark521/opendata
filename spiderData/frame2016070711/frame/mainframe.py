# -*- coding: cp936 -*-
from tkinter import *
import os
from tkinter.messagebox import *
import time
from logtext import *

#����������ݲ����ķ�������

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
    
    def __init__(self, title='���ݿ�����ĿУ��', width=500, height=300):
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
        Label(self.root, text='ѡ������Դ',pady = 0, font=('Arial', 15)).place(rely = lineLen*0, relheight = lineLen, relwidth = lineLen)
        
        self.btnWH = Button(self.root,command = lambda:self.selectSource('wh'),text='�人����', font=('Arial', 15), width=15, height=2)
        self.btnSH = Button(self.root,command = lambda:self.selectSource('sh'),text='�Ϻ�����', font=('Arial', 15), width=15, height=2)
        self.btnBJ = Button(self.root,command = lambda:self.selectSource('bj'),text='��������', font=('Arial', 15), width=15, height=2)
        self.btnCL = Button(self.root,text='����', width=15, height=2)

        self.btnWH.place(rely = lineLen*1, relheight = lineLen, relwidth = lineLen)
        self.btnSH.place(rely = lineLen*2, relheight = lineLen, relwidth = lineLen)
        self.btnBJ.place(rely = lineLen*3, relheight = lineLen, relwidth = lineLen)

        Label(self.root, text='����Դ',bg='red' ,borderwidth=1, font=('Arial', 15), width=15, height=2).place(relx = lineLen, relwidth = lineLen, relheight = lineLen)
        self.source = StringVar()
        self.source.set('δѡ��')
        Label(self.root,textvariable = self.source, font=('Arial', 15),bg='yellow', width=15, height=2).place(relx = lineLen*2, relwidth = lineLen, relheight = lineLen)
        self.lb_int = Text(self.root, font =('Verdana',12), width=40)#, width=65, height=20
        #self.lb_int.bind('<Button-1>', self.get_int,)
        self.scrl_int = Scrollbar(self.root)
        self.scrl_int.place(relx = 1- 0.04,rely = lineLen, relwidth = 0.04, relheight = 0.8)
        self.lb_int.configure(yscrollcommand = self.scrl_int.set)
        self.lb_int.place(relx = lineLen, rely = lineLen,relwidth = 1 - lineLen - 0.04, relheight = 1 - lineLen)
        self.scrl_int['command'] = self.lb_int.yview

        self.match = Button(self.root, text = 'ƥ������', font=('Arial', 15), command=self.matchData)
        self.match.place(relx = lineLen*4, relwidth = lineLen, relheight = lineLen)
        
        self.loaddata = Button(self.root, text='��ȡ����', font=('Arial', 15),command=self.downloaddata)
        self.loaddata.place(relx = lineLen*3, relwidth = lineLen, relheight = lineLen)
       
    #�������ݳ�ʼ��
    def downloaddata(self):
        if self.city == None:
            showinfo(title='��ʾ��Ϣ',message='��δѡ������Դ')
        elif self.city == 'bj':
            downBJ(self)
        elif self.city == 'sh':
            downSH(self)
        elif self.city == 'wh':
            downWH(self)
        else:
            showinfo(title='��ʾ��Ϣ',message='���Ǳ�������')

    #��������ƥ�����ĳ�ʼ�������ݵ���ȡ
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
        #����ƥ�����
        linx = 0.001
        liny = 0.01
        
        xpos = 0.2 + linx
        ypos = 0.2
        xlen = 0.266666
        ylen = 0.3
        #��������
        Label(self.top, text='������Ŀ',font=('Arial', 15),borderwidth = 3,bg='#B8CCE4').place(relx=0.2, relheight=xpos, relwidth=xlen)
        Label(self.top, text='������Դ',font=('Arial', 15),borderwidth = 3).place(relx=0.466666, relheight=xpos, relwidth=xlen)
        Label(self.top, text='�ṩ����',font=('Arial', 15),borderwidth = 3,bg='#B8CCE4').place(relx=0.73332, relheight=xpos, relwidth=xlen)
        firCity = StringVar()
        firCity.set('������Ŀ')
        Label(self.top,textvariable = firCity ,font=('Arial', 15),anchor = 'e',bg='#B8CCE4').place(rely=ypos, relheight=0.3, relwidth=ypos)
        secCity = StringVar()
        secCity.set('�人��Ŀ')
        Label(self.top,textvariable = secCity,font=('Arial', 14),anchor = 'e').place(rely=ypos + ylen, relheight=xpos, relwidth=ypos)

        #��ʾ��Ϣ
        self.pageMessage = StringVar()
        Label(self.top, textvariable = self.pageMessage, font=(('Arial', 12)),anchor='e').place(rely=ypos + 2*ylen, relheight=xpos, relwidth=ypos + 0.1)

        #�����жϰ�ť
        check = PhotoImage(file = 'check.png')
        error = PhotoImage(file = 'error.png')
        Button(self.top, image = check,command=self.bingoData).place(relx = 0.5-0.08 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.08)
        Button(self.top, image = error,command=self.errorData).place(relx = 0.5 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.08)

        #��һ����һ����ť
        Button(self.top, text = '��һ��',command=self.pre_topData, width=30, height=30).place(relx = 0.7 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.1)
        Button(self.top, text = '��һ��',command=self.next_topData, width=30, height=30).place(relx = 0.8 , rely = ypos+2*ylen, relheight=ypos, relwidth=0.1)

        #�м�����ֵ
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

        #�������Գ�ʼ��
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
        return '��ǰ��'+str(currentPage + 1)+'ҳ,��'+str(totolPage)+ 'ҳ'

    #��ƥ�䵽��ͬ�����ݺ���еĲ���
    def bingoData(self):
        temp = []
        temp.insert(0, self.data[self.index_data])
        temp.insert(1, self.other[self.index_data])
        if temp in self.diff_data:
            self.diff_data.remove(temp)
            print('�Ӳ�ͬɾ��')
        if temp not in self.same_data:
            self.same_data.append(temp)
            print('����ͬ���')
        self.next_topData()
    #��ƥ�䵽��ͬ������
    def errorData(self):
        temp = []
        temp.insert(0, self.data[self.index_data])
        temp.insert(1, self.other[self.index_data])
        if temp not in self.diff_data:
            self.diff_data.append(temp)
            print('�Ӳ�ͬ���')
        if temp in self.same_data:
            self.same_data.remove(temp)
            print('����ͬɾ��')
        self.next_topData()

    #��ȡ��һ������
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
            showinfo(title='��ʾ��Ϣ',message='���ƥ��')
            print(len(self.diff_data))
            for e in self.diff_data:
                print(e[0].name, e[1].name)
            for e in self.same_data:
                print(e[0].name, e[1].name)
            print(len(self.same_data))
            self.top.destroy()
            
    #��ȡǰһ������
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
            showinfo(title='��ʾ��Ϣ',message='�Ѿ��ǵ�һ������')
            #self.top.destroy()

    #ѡ������Դ
    def selectSource(self, city):
        if self.stat == True:
            s = ''
            self.city = city
            if city == 'sh':
                s = '�Ϻ�����'
            if city == 'bj':
                s = '��������'
            if city == 'wh':
                s = '�人����'
            self.source.set(s)
        else:
            showinfo(title='��ʾ��Ϣ',message='���ڽ������ݷ���...')
             
    def event(self):
        self.btnSer['state'] = 'disabled'
        if self.stat:
            self.btnSer['text'] = '��������'
            self.stat = False
            self.root.iconbitmap(self.stoIco)
        else:
            self.btnSer['text'] = 'ֹͣ����'
            self.stat = True
            self.root.iconbitmap(self.staIco)
        self.btnSer['state'] = 'active'
    #��ǰ�ı�������ı�
    def systemPrint(self, s):
        col = len(s)
        logging.info(s)
        self.lb_int.insert(END, s + '\n')
        
        time.sleep(0.1)
        self.lb_int.update()
        self.lineNum +=1
        self.lb_int.see(str(float(self.lineNum)))
        
    
    def loop(self):
        self.root.resizable(False, False)   #��ֹ�޸Ĵ��ڴ�С

        self.packBtn()
        self.center()                       #���ھ���
        #self.event()
        self.root.mainloop()


#####################################################################################



if __name__ == '__main__':
    initLogging('myapp.log')
    w = Window()
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()

'''#���ر�������
def downdBJ(window):
    #�������ݰ����⻮�ֵĽ�������
    aztUrl = "http://www.bjdata.gov.cn/zyml/azt/lyzs/zs/index.htm"
    #�������ݰ��������ֵĽ�������
    ajgUrl = "http://www.bjdata.gov.cn/zyml/ajg/"
    #��ȡ���п������ݵ���������
    result = getFromGov(ajgUrl + "sjw/index.htm")
    result.insert(0,('sjw/index.htm', '�н�ί', '6'))
    #��ȡ�����������ݵ��������,��������б���
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

    #��������Ϣ���浽����
    classList = []
    for each in infoList:
        temp = Data(each[2],each[1], each[0], 'BJ')
        classList.append(temp)
    window.systemPrint('���ݷ�����...')
    saveAsPKL(classList, 'BJEntry')
    window.systemPrint('���ݱ���ɹ�')


#�����Ϻ���������Ϣ
def downloadSH(window):
    url = "http://www.datashanghai.gov.cn/query!"
    #���ݽӿ�url
    productPageUrl = "queryProduct.action?currentPage="
    #Ӧ�ýӿ�url
    appPageUrl = "queryApp.action?currentPage="
    #�ӿ���Ϣurl
    interfacePageUrl = "queryInterface.action?currentPage="
    currentPage = 1
    #���ݽӿ�url
    productLinkedList = []
    #Ӧ�ýӿ�url
    appLinkedList = []
    #�ӿ���Ϣurl
    interfaceLinkedList = []
    #��������������Ŀ
    productLinkedList = getAllLinked(productPageUrl, "����")
    appLinkedList = getAllLinked(appPageUrl, "Ӧ��")
    interfaceLinkedList = getAllLinked(interfacePageUrl, "�ӿ�")

    print('��ʼץȡ����')
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
    #saveAsCSV(ll, "�Ϻ�Ӧ�ÿ���")
    print('ץȡ���ݳɹ�')
    classList = []
    for each in infoList:
        temp = Data(each[2],each[1], each[0], 'SH')
        classList.append(temp)
    print('���ݷ�����...')
    saveAsPKL(classList, './data/SHEntry')
    print('���ݱ���ɹ�')


#�����人������Ϣ
def dowmloadWH(window)
    #�人���ݿ����б����ҳ��
    listUrl = 'http://www.wuhandata.gov.cn/whdata/resources_listPage.action'
    infoUrl = 'http://www.wuhandata.gov.cn/whdata/resources_list.action?category=25bde262-31b4-4901-8d53-527631005f6a&pageNum='

    #��ȡ���ݿ��ŵ���Ŀ,�������Ż����Ϳ�����Ŀ
    orgResult, resResult = getResourceId(listUrl)

    #���ڴ洢�������ݿ��ŵ���Ŀ
    dataList = []

    #������Ҳ����ѭ����ȡ
    page = 1
    dataInfo = getAllPageLinked(infoUrl + str(page))
    totlePage = dataInfo['pages']
    dataList.extend(getInfoFromJson(dataInfo['list']))
    while(dataInfo['hasNextPage'] == True):
        page = page + 1
        print('��'+str(totlePage)+'ҳ,�����������ص�' +str(page) + "ҳ" )
        dataInfo = getAllPageLinked(infoUrl + str(page))
        dataList.extend(getInfoFromJson(dataInfo['list']))


    #��������Ϣ���浽����
    classList = []
    for each in dataList:
        temp = Data(each[3],each[2], each[0], 'WH')
        classList.append(temp)
    print('���ݷ�����...')
    saveAsPKL(classList, './data/WHEntry')
    print('���ݱ���ɹ�')
def matchL(window):
    #����������,Ϊ�ؼ��ּ�����׼��
    window.systemPrint('����������...')
    dataBJ = readFromPKL(filenameBJ)
    dataWH = readFromPKL(filenameWH)
    dataSH = readFromPKL(filenameSH)
    
    #�Լ������ݽ��г�ʼ��
    entryBJ = initEntryFromData(dataBJ)
    entryWH = initEntryFromData(dataWH)
    entrySH = initEntryFromData(dataSH)
    time.sleep(0.1)
    window.systemPrint('�����������')
    time.sleep(0.1)
    return entryBJ, entrySH
'''
