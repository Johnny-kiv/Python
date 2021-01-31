#Это тренировка

from tkinter import*
root=Tk()
m=Menu(root)
root.config(menu=m)
fm=Menu(m)
def h(event):
    print('Hello, world')
def mat():
    but1=Button(root)
    but1["text"]="канкулятор"
    but1.bind("<Button-1>",h )
    but1.pack()
    but1=Button(root)
    but1["text"]="1 класс"
    but1.bind("<Button-1>",h )
    but1.pack()
m.add_cascade(label='Учебники',menu=fm)
fm.add_command(label='Математика',command=mat)
fm.add_command(label='Математика',command=russ)

root.mainloop()
