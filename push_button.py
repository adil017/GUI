from tkinter import*
def buttonclick(self):
    print("Hi there!")
root=Tk()
root.title("Interface")
f=Frame(root,height=200,width=300)
f.propagate(0)
f.pack()
b=Button(f,text='adil',width=15,height=2,bg='red')
b.pack()
b.bind("<Button-3>",buttonclick)
root.mainloop()