#Это тренировка]
from tkinter import*
def n():
    fra1 = Frame(root, width=1000, height=100, bg="darkred")
    fr = Text(root, width=100, height=10, wrap=WORD, bg="white")
    fra1.pack()
    fr.pack()
    root.mainloop()

root=Tk()
m= Menu(root)
root.config(menu=m)
fm=Menu(m)
m.add_cascade(label="файл",menu=fm)
fm.add_cascade(label="Создать",command=n)
fra1= Frame(root,width=1000,height=100,bg="darkred")
fr=Text(root,width=100,height=10,wrap=WORD,bg="white")
fra3= Frame(root,width=500,height=150,bg="darkblue",bd=20)
fra1.pack()
fr.pack()
root.mainloop()
