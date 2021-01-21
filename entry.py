from tkinter import*
class xyz:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=350)
        self.f.propagate(0)
        self.f.pack()
        self.l1=Label(text="Enter your name:")
        self.l2=Label(text="Enter password:")
        self.e1=Entry(self.f,width=20,font=('Arial',16))
        self.e2=Entry(self.f,width=20,show='*')
        self.e2.bind("<Return>",self.display)
        self.l1.place(x=50,y=100)
        self.e1.place(x=150,y=100)
        self.l2.place(x=50,y=150)
        self.e2.place(x=150,y=150)
    def display(self,event):
        str1=self.e1.get()
        str2=self.e2.get()
        lb1=Label(text="Your name is:"+str1).place(x=50,y=200)
        lb2=Label(text="Your password is:"+str2).place(x=50,y=220)
root=Tk()
root.title("Entry of things")
eb=xyz(root)
root.mainloop()

