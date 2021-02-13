#Это напоминальщик 
#версия 2
#Автор: johnny-kiv  
from tkinter import*
root=Tk()
c=Canvas(root,bg="grey",width=800,height=600)
c.pack()

import time

a2=int(input("Введите минуты работы: "))
b2=int(input("Введите минуты отдыха: "))
if a2==0:
    a4=20*60
if b2==0:
    b4=20*60
else:
    a4=a2*60
    b4=b2*60
r=1

c.create_text(500,50,text="Работаем",fill="green")

while r:
    time.sleep(a4)
    c.create_text(500,50,text="Отдыхаем.",fill="green")

    time.sleep(b4)

    c.create_text(500,50,text="Работаем",fill="green")
    root.mainloop()