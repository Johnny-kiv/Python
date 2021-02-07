from tkinter import*
class Paint(Frame):
    def _init_(self,parent):
        Frame._init_(self):
        self.parent=parent
        self.brush_size=10
        self.brush_color="white"
        self.color="white"
        self.setUI()
    def draw(self,event):
        self.canv.create_oval(event.x-self.brush_size,event.y-self.brush_size,event.x+self.brush_size,event.y+self.brush_size,fill=self.color,outline=self.color)
    def set_color(self,new_color):
        self.color=new_color
    def set_brush_size(self,new_size):
        self.brush_size=new_size
    def setUI(self):
        self.parent.title("Anti Paint")
        self.pack(fill=BOTH,expand=1)
        self.columconfigure(6,weight=1)
        self.columconfigure(2,weight=1)
        self.canv=Canvas(sefl.bg="black")
        self.canv.grid(row=2,column=0,columnspan=7,padx=5,pady=5,sticky=E+W+S+N)
        self.canv.bind("<B1-Motion>",self.draw)
        color_lab=Label(self,,text="Цвет")
        color_lab.grid(row=0,column=0,padx=6)
        red_btn=Button(self,text="Красный",width=10,command=lambda:self.set_color("red"))
        red_btn.grid(row=0,column=1,sticky=W)
        color_lab=Label(self,,text="Размер кисти")
        color_lab.grid(row=0,column=0,padx=6)
        red_btn=Button(self,text="2х",width=10,command=lambda:self.set_brush_size(2))
        red_btn.grid(row=1,column=1,sticky=W)
    def main():
        root=Tk()
        root.geometry("800x600+300+300")
        app = Paint(root)
        root.mainloop()
name="_main_"
if name=="_main_":
    main()
