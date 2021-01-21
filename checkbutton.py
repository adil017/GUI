from tkinter import *
class checkbutton:
    def __init__(self, root):
        self.f=Frame(root,height=350,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.c1=Checkbutton(self.f,bg='red',fg='blue',font=('Arial',16,'underline'),text='Java',variable=self.var1,command=self.display)
        self.c2=Checkbutton(self.f,bg='green',fg='yellow',font=('Arial',16,'underline'),text='Python',variable=self.var2,command=self.display)
        self.c3=Checkbutton(self.f,bg='green',fg='yellow',font=('Arial',16,'underline'),text='Javascript',variable=self.var3,command=self.display)
        self.c1.place(x=250,y=250)
        self.c2.place(x=350,y=250)
        self.c3.place(x=450,y=250)
    def display(self):
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()
        str=''
        if x==1:
            str+='Java'
        if y==1:
            str+='Python'
        if z==1:
            str+='Javascript'
        lb1=Label(text=str,fg='Black').place(x=50,y=150,width=200,height=20)
        
root=Tk()
root.title("add")
mb=checkbutton(root)
root.mainloop()