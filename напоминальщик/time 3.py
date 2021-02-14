#Это напоминальщик 
#версия 2
#Автор: johnny-kiv  

#Подключаем модули tkinter, time и дополнительный модуль messagebox
from tkinter import*
from tkinter import messagebox  
import time
root=Tk()
#Подключаем виджет Canvas
c=Canvas(root,bg="grey",width=800,height=600)
c.pack()
a2=IntVar()
b2=IntVar()
c2=IntVar()
def begin():
    if a2==0:
        a4=20*60
    if b2==0:
        b4=20*60
    else:
        a4=a2*60
        b4=b2*60
    r=0
    c.create_text(500,50,text="Работаем",fill="green")
    for r in range(c2):
        time.sleep(b4)
        messagebox.showinfo("Отдыхаем")
        time.sleep(a4)
        messagebox.showinfo("Работаем")

a2l=Label(text="Введите минуты работы: ")
a2l.grid(row=0,column=0,sticky="w")
a2e=Entry(textvariable=a2)
a2e.grid(row=0,column=1,sticky="e")
b2l=Label(text="Введите минуты отдыха: ")
a2l.grid(row=1,column=0,sticky="w")
b2e=Entry(textvariable=b2)
b2e.grid(row=1,column=1,sticky="e")
с2l=Label(text="Введите сколько раз вы будете работать или отдыхать: ")
с2l.grid(row=2,column=0,sticky="w")
с2e=Entry(textvariable=c2)
с2e.grid(row=2,column=1,sticky="e")

btn=Button(text="Начать",command=begin)
btn.grid(row=3,column=0,sticky="w")


a2l.pack()
a2e.pack()
b2l.pack()
b2e.pack()
c2l.pack()
c2e.pack()
btn.pack()

root.mainloop()