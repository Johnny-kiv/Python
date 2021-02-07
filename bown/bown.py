from tkinter import*
import random
win=Tk()
c=Canvas(win,width=800,height=650,bg="grey",cursor="pencil")
c.pack()

x = random.randint(1, 790)
z=c.create_oval(x, x, x + 100, x + 100, fill="red")

win.mainloop()
