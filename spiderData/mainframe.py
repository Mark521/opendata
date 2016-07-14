# -*- coding: cp936 -*-
from tkinter import *
import os
from tkinter.messagebox import *

class Window:
    def __init__(self, title='���ݿ�����ĿУ��', width=600, height=500, staFunc=bool, stoFunc=bool):
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

        #�����
        self.frm_L = Frame(self.frm)
        self.frm_LT = Frame(self.frm_L)
        Label(self.frm_L, text='ѡ������Դ',pady = 0, font=('Arial', 15)).pack(side=TOP)
        self.btnSer = Button(self.frm_LT, command=self.event, width=15, height=2)
        self.btnWH = Button(self.frm_LT,command = lambda:self.selectSource('wh'),text='�人����', width=15, height=2)
        self.btnSH = Button(self.frm_LT,command = lambda:self.selectSource('sh'),text='�Ϻ�����', width=15, height=2)
        self.btnBJ = Button(self.frm_LT,command = lambda:self.selectSource('bj'),text='��������', width=15, height=2)
        self.btnCL = Button(self.frm_LT,text='����', width=15, height=2)
        self.btnSer.pack(padx=10, side=TOP)
        
        self.btnWH.pack(padx=10, side=TOP)
        self.btnSH.pack(padx=10, side=TOP)
        self.btnBJ.pack(padx=10, side=TOP)
        self.frm_LT.pack(side=TOP,fill='both')
        self.frm_L.pack(side=LEFT)

        #�ҽ���
        self.frm_R = Frame(self.frm)
        self.frm_RT = Frame(self.frm_R)
        Label(self.frm_RT, text='����Դ', font=('Arial', 15)).pack(side=LEFT)
        self.source = Label(self.frm_RT,text='δѡ��', font=('Arial', 15))
        self.source.pack(side=LEFT)
        self.loaddata = Button(self.frm_RT, text='��ȡ����',command=self.downloaddata, width=15, height=2)
        self.match = Button(self.frm_RT, text = 'ƥ������', command=self.matchData, width=15, height=2 )
        self.loaddata.pack(side=LEFT)
        self.frm_RT.pack(side=TOP)
        
        self.frm_R.pack(side=RIGHT)
        
        self.frm.pack()

    #�������ݳ�ʼ��
    def downloaddata(self):
        if self.city == None:
            showinfo(title='��ʾ��Ϣ',message='��δѡ������Դ')
        elif self.lb_int == None:
            #��ʾ��ǰ�Ľ���
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
            #���õ�ǰ���ڲ��ܽ�����������
            self.stat = False
        else:
            showinfo(title='��ʾ��Ϣ',message='���ڽ������ݷ���')
            self.lb_int.pack_forget()
            self.scrl_int.pack_forget()
            self.match.pack_forget()
            self.lb_int = None
            self.city = None
            self.match = None
            self.source['text'] = 'δѡ��'
            self.stat = True

    def matchData(self):
        self.top = Toplevel()
        
        #�����
        self.top_frm_T = Frame(self.top)
        Label(self.top_frm_T, text='������Ŀ1', font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_T, text='������Ŀ2', font=('Arial', 15)).pack(side=LEFT)

        self.top_frm_M = Frame(self.top)
        Label(self.top_frm_M, text='������Ŀ3',padx = 10, font=('Arial', 15)).pack(side=RIGHT)
        Label(self.top_frm_M, text='������Ŀ4',padx = 10, font=('Arial', 15)).pack(side=RIGHT)

        self.top_frm_B = Frame(self.top)
        Label(self.top_frm_B, text='������Ŀ5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_B, text='������Ŀ5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_B, text='������Ŀ5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        Label(self.top_frm_B, text='������Ŀ5',pady = 0, font=('Arial', 15)).pack(side=LEFT)
        
        self.top_frm_T.pack(side=TOP)
        self.top_frm_M.pack(side=TOP)
        self.top_frm_B.pack(side=TOP)

        self.top.mainloop()
    
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
            self.source['text'] = s
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
    def systemPrint(self, s):
        self.lb_int.insert(END,s)
    
    def loop(self):
        self.root.resizable(False, False)   #��ֹ�޸Ĵ��ڴ�С
        self.packBtn()
        self.center()                       #���ھ���
        #self.event()
        self.root.mainloop()
#####################################################################################




if __name__ == '__main__':
    w = Window(staFunc=bool, stoFunc=bool)
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()
