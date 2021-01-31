

from tkinter import*
root=Tk()
m=Menu(root)
root.config(menu=m)
fm=Menu(m)
def h():
    
def mat():
   but1=Button(root)
   but1=["text"]="канкулятор"
   
   but1.pack()
m.add_cascade(label='Книги',menu=fm)
fm.add_command(label='Математика',command=mat)

root.mainloop()
