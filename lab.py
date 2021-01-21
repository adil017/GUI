from tkinter import*
import array as arr
class MyButtons:
    def __init__(self,root):
        self.f=Frame(root,height=300,width=550)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f,text="Click here",height=2,width=15,command=self.buttonClick,bg="green")
        self.b2=Button(self.f,text='Close',height=2,width=15,command=quit,bg="red")
        self.b1.grid(row=0,column=1)
        self.b2.grid(row=0,column=2)
    def buttonClick(self):
        print("hi there")
        self.lb1=Label(self.f,text="Welcome to my house",width=20,height=2,font=('Courier',-30,'bold underline'),fg='blue',bg='black')
        self.lb1.grid(rows=2,column=0)
root=Tk()
root.title("Interface")
mb=MyButtons(root)
root.mainloop()