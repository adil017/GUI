from tkinter import*
class MyButton:
    def __init__(self,root):
        self.f=Frame(root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f,text='Red',width=15,height=2,command=lambda:self.buttonClick(1))
        self.b2=Button(self.f,text='Green',width=15,height=2,command=lambda:self.buttonClick(2))
        self.b3=Button(self.f,text='Blue',width=15,height=2,command=lambda:self.buttonClick(3))
        self.b1.grid(row=0,column=1,padx=10,pady=15)
        self.b2.grid(row=1,column=2,padx=15,pady=20)
        self.b3.grid(row=2,column=3,padx=10,pady=20)
    def buttonClick(self,num):
        if num==1:
            self.f["bg"]='Red'
        if num==2:
            self.f["bg"]='Green'
        if num==3:
            self.f["bg"]='Blue'
root=Tk()
root.title("add")
mb=MyButton(root)
root.mainloop()