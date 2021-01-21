from tkinter import*
class add:
    def __init__(self,root):
       self.f=Frame(root,height=350,width=500)
       self.f.propagate(0)
       self.f.pack()
       self.val1=IntVar()
       self.val2=StringVar()
       self.s1=Spinbox(self.f,from_=1,to=10,textvariable=self.val1,width=15,bg='blue',font=('Arial',14,'underline'))
       self.s2=Spinbox(self.f,values=('Delhi','Lucknow','Bangalore','Kolkata','Chennai'),textvariable=self.val2,width=15,bg='red',font=('Arial',14,'bold'))
       self.b=Button(self.f,text='get value from spinbox',command=self.display)
       self.s1.place(x=150,y=150)
       self.s2.place(x=150,y=180)
       self.b.place(x=50,y=230)
    def display(self):
        str1=self.val1.get()
        s=self.val2.get()
        lb1=Label(text='selected value is: '+str(str1)).place(x=50,y=200)
        lb2=Label(text='selected city is: '+s).place(x=50,y=220)
root= Tk()
root.title("Spin the value")
mb=add(root)
root.mainloop()