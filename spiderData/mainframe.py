# -*- coding: cp936 -*-
from tkinter import *
import os
from tkinter.messagebox import *

class Window:
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

        #左界面
        self.frm_L = Frame(self.frm)
        self.frm_LT = Frame(self.frm_L)
        Label(self.frm_L, text='选择数据源',pady = 0, font=('Arial', 15)).pack(side=TOP)
        self.btnSer = Button(self.frm_LT, command=self.event, width=15, height=2)
        self.btnWH = Button(self.frm_LT,command = lambda:self.selectSource('wh'),text='武汉数据', width=15, height=2)
        self.btnSH = Button(self.frm_LT,command = lambda:self.selectSource('sh'),text='上海数据', width=15, height=2)
        self.btnBJ = Button(self.frm_LT,command = lambda:self.selectSource('bj'),text='北京数据', width=15, height=2)
        self.btnCL = Button(self.frm_LT,text='重置', width=15, height=2)
        self.btnSer.pack(padx=10, side=TOP)
        
        self.btnWH.pack(padx=10, side=TOP)
        self.btnSH.pack(padx=10, side=TOP)
        self.btnBJ.pack(padx=10, side=TOP)
        self.frm_LT.pack(side=TOP,fill='both')
        self.frm_L.pack(side=LEFT)

        #右界面
        self.frm_R = Frame(self.frm)
        self.frm_RT = Frame(self.frm_R)
        Label(self.frm_RT, text='数据源', font=('Arial', 15)).pack(side=LEFT)
        self.source = Label(self.frm_RT,text='未选择', font=('Arial', 15))
        self.source.pack(side=LEFT)
        self.loaddata = Button(self.frm_RT, text='读取数据',command=self.downloaddata, width=15, height=2)
        self.match = Button(self.frm_RT, text = '匹配数据', command=self.matchData, width=15, height=2 )
        self.loaddata.pack(side=LEFT)
        self.frm_RT.pack(side=TOP)
        
        self.frm_R.pack(side=RIGHT)
        
        self.frm.pack()

    #进行数据初始化
    def downloaddata(self):
        if self.city == None:
            showinfo(title='提示信息',message='还未选择数据源')
        elif self.lb_int == None:
            #显示当前的进程
            self.var_R_int = StringVar()
            self.lb_int = Listbox(self.frm_R, selectmode=BROWSE, listvariable=self.var_R_int, font =('Verdana',12), width=65, height=20)
            #self.lb_int.bind('<Button-1>', self.get_int,)
            self.scrl_int = Scrollbar(self.frm_R)
            self.scrl_int.pack(side=RIGHT, fill=Y)
            self.lb_int.configure(yscrollcommand = self.scrl_int.set)
            self.lb_int.pack(side=LEFT, fill=BOTH)
            self.scrl_int['command'] = self.lb_int.yview
            self.systemPrint('s')
            self.match.pack(side=LEFT)
            #设置当前窗口不能进行其他操作
            self.stat = False
        else:
            showinfo(title='提示信息',message='正在进行数据分析')
            self.lb_int.pack_forget()
            self.scrl_int.pack_forget()
            self.match.pack_forget()
            self.lb_int = None
            self.city = None
            self.match = None
            self.source['text'] = '未选择'
            self.stat = True

    def matchData(self):
        self.top = Toplevel()
        
        #左界面
        self.top_frm_T = Frame(self.top)
        Label(self.top_frm_T, text='数据条目1', font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_T, text='数据条目2', font=('Arial', 15)).pack(side=LEFT)

        self.top_frm_M = Frame(self.top)
        Label(self.top_frm_M, text='数据条目3',padx = 10, font=('Arial', 15)).pack(side=RIGHT)
        Label(self.top_frm_M, text='数据条目4',padx = 10, font=('Arial', 15)).pack(side=RIGHT)

        self.top_frm_B = Frame(self.top)
        Label(self.top_frm_B, text='数据条目5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_B, text='数据条目5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_B, text='数据条目5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_B, text='数据条目5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        
        self.top_frm_T.pack(side=TOP)
        self.top_frm_M.pack(side=TOP)
        self.top_frm_B.pack(side=TOP)

        self.top.mainloop()
    
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
            self.source['text'] = s
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
        self.lb_int.insert(END,s)
    
    def loop(self):
        self.root.resizable(False, False)   #禁止修改窗口大小
        self.packBtn()
        self.center()                       #窗口居中
        #self.event()
        self.root.mainloop()
#####################################################################################




if __name__ == '__main__':
    w = Window(staFunc=bool, stoFunc=bool)
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()
