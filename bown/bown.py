from tkinter import*
import random
import time
win=Tk()
win.title("Bown")
c=Canvas(win,width=1000,height=610,bg="grey",cursor="pencil")
c.create_text(500,20,text="Правила игры очень просты: просто ловиш шарик.Если сочетания клавиш ctr-v, то вправоо,а лево ctr-c,а если нажмёш пробел то шарик будет падать.",fill="green")
r=c.create_polygon(500,600,[550,550,],[450,550],fill="green")
r2=c.create_oval(100,100,150,150,fill="blue")
def l(event):
    c.move(r,-10,0)
def p(event):
    c.move(r,10,0) 
def lb(event):
    c.move(r2,0,10)
class Bown(object):
    def _init_(self):
        win.bind('<Control-c>',l)
        win.bind('<Control-v>',p)
kor=Bown()
kor._init_()   
class V(object):
    def _init_(self):
        win.bind('<space>',lb)
k=V()
k._init_()   
c.pack()
win.mainloop()
