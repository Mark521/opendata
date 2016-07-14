from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.messagebox import *


#打开文件
def openFile():
  global fname
  fname = askopenfilename(filetypes=(("Template files", "*.xls;*.xlsx"),("HTML files", "*.html;*.htm"),("All files", "*.*") ))
  print(fname)
  isTrueFile
#判断文件格式是否正确
def isTrueFile():
  showinfo(title='提示信息',message=fname)

fname = ''
root = Tk(className='表格数据合并')


Button(root, command=openFile, text='选择文件', font=('Arial', 15), width=15, height=2).pack()


root.mainloop()
