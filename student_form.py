from tkinter import*
class add:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=300)
        self.f.propagate(0)
        self.f.pack()
        #Creating entry widget for name,last
        self.lb1=Label(text="First Name:")
        self.lb2=Label(text="Last Name:")
        self.e1=Entry(self.f,width=16,font=('Arial',16))
        self.e2=Entry(self.f,width=16,font=('Arial',16))
        self.e2.bind("<Return>",self.display)
        self.lb1.place(x=50,y=100)
        self.e1.place(x=120,y=100)
        self.lb2.place(x=50,y=150)
        self.e2.place(x=120,y=150)
    #Creating a spinbox for age
        self.val1=IntVar()
        self.l1=Label(text="Age:")
        self.s1=Spinbox(self.f,from_=1,to=100,textvariable=self.val1,width=15,bg='blue',font=('Arial',14,'underline'))
        self.l1.place(x=50,y=200)
        self.s1.place(x=120,y=200)
     #Create a radiobutton for age
        self.var=IntVar()
        self.l2=Label(text="Gender:")
        self.r1=Radiobutton(self.f,font=('Georgia',16),text='Male',command=self.display)
        self.r2=Radiobutton(self.f,font=('Georgia',16),text='Female',command=self.display)
        self.l2.place(x=50,y=250)
        self.r1.place(x=120,y=240)
        self.r2.place(x=120,y=280)
        self.b=Button(self.f,text='Submit',width=15,height=2,command=self.display)
        self.b.grid(padx=355,pady=390)
    def display(self,event):
        str1=self.e1.get()
        str2=self.e2.get()
        a=self.s1.get()
        s=self.r1.get()
        e=self.r2.get()
        str=' '
        if s==1:
            str+='You selected:Male'
        if str==2:
            str+='You selected:Female'
        l3=Label(text=str,fg='blue').place(x=150,y=300,width=200,height=20)
root=Tk()
root.title("student form")
mb=add(root)
root.mainloop()

