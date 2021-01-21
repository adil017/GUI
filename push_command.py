from tkinter import*
class Adil:
     def __init__(self, root):
          
        self.f=Frame(root,height=300,width=300)
        self.f.propagate(0)
        self.f.pack()
        self.b=Button(self.f, text='CR7', width=25, height=5, bg='red', fg='black', activebackground='green', activeforeground='blue',command=self.Buttonclick)
        self.b.pack()
     def Buttonclick(self):
         print("Hi there")
root= Tk()
root.title("Interface")
mb = Adil(root)
root.mainloop()