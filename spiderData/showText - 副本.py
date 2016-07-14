from tkinter import *

root = Tk()
root.geometry('400x300')
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
mylist.insert(END, '这是哈哈哈哈')
mylist.insert(END, "This is line number " + str(0))
for line in range(2,100):
   mylist.insert(END, "This is line number " + str(line))
   #mylist.after(1000)

mylist.pack( side = RIGHT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()
