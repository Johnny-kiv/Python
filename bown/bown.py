from tkinter import*
import random
win=Tk()
c=Canvas(win,width=800,height=650,bg="grey",cursor="pencil")
c.pack()
x=random.randint(1,790)
a=1
rect=c.create_oval(x,100,x+50,150,fill="red")
c.move(rect,0,150)

win.mainloop()
