from tkinter import *
def onGo():
    def counter(i):
        if i > 0:
            text.insert(END,'a_'+str(i) + '\n')
            text.after(1000, counter, i-1)
        else:
            goBtn.config(state=NORMAL)
        goBtn.config(state=DISABLED)
    counter(10)
                  
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
#root.geometry('400x300')
text = Text(root, width=20, height=5, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config( command = text.yview )
goBtn = Button(text = "Go!",command = onGo)
goBtn.pack()
root.mainloop()
