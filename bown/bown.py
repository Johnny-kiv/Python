from tkinter import*
import random
import time
win=Tk()
win.title("Bown")
c=Canvas(win,width=1000,height=610,bg="grey",cursor="pencil")
c.create_text(500,20,text="Правила игры очень просты: просто ловиш шарик.Если сочетания клавиш ctr-v, то вправоо,а лево ctr-c,а если нажмёш пробел то шарик будет падать.",fill="green")
r=c.create_polygon(350,550,[450,550,],[400,599],fill="green")
def l(event):
    c.move(r,-10,0)
def p(event):
    c.move(r,10,0)


win.bind('<Control-c>',l)
win.bind('<Control-v>',p)
t=random.randint(1,799)
u=c.create_oval(t,35,t+50,85,fill="green")
y=10
while y<9:
    c.move(u,0,10)
    y=y+1
c.pack()
win.mainloop()
