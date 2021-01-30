#class Snake(object):
#    def bing(self):
#        print('\a'
from tkinter import*
root=Tk()
ent=Entry(root,width=50)
lbl=Label(root,width=50)
def exit_(event):
    root.destroy()
def caption(event):
    t=ent.get()
    lbl.configure(text=t)

ent.bind('<Return>',caption)
root.bind('<Control-z>',exit_)
ent.pack()
lbl.pack()
