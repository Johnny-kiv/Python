from tkinter import*
import random
import time
win=Tk()
win.title("Bown")
c=Canvas(win,width=1000,height=610,bg="grey",cursor="pencil")
c.create_text(500,20,text="Правила игры очень просты: просто ловиш шарик.",fill="green")
r=c.create_polygon(500,600,[550,550,],[450,550],fill="green")
def l(event):
    c.move(r,-10,0)
def p(event):
    c.move(r,10,0) 
class Bown(object):
    def _init_(self):
        win.bind('<Left>',l)
        win.bind('<Right>',p)
kor=Bown()
kor._init_()   
class V(object):
    def _init_(self):
        a=random.randint(1,990)
        r2=c.create_oval(a,50,a+50,100,fill="blue")
        time.sleep(1)
        c.coords(r2,a,602,a+50,652)
        r1=1
k=V()
k._init_()   
c.pack()
win.mainloop()
