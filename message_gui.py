from tkinter import*
class MyMsg:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=300)
        self.f.propagate(0)
        self.f.pack()
        self.m=Message(self.f,text="Hello my name is adil ahmad i am studying in galgotias college and i am doin mca",width=200,font=('Times New Roman',20,'bold italic underline'),fg='blue')
        self.m.pack(side=LEFT,padx=15,pady=20)
root=Tk()
root.title("Interface")
mb=MyMsg(root)
root.mainloop()