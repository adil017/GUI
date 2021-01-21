from tkinter import*
from tkinter import font
root=Tk()
root.title("INTER")
fnt=('Times',96,'bold italic underline')
print(fnt)
c=Canvas(root,bg="red",height=900,width=1000,cursor='pencil')
id=c.create_text(500,100,text="adil",font=fnt,fill="yellow",activefill="black")
c.pack()
root.mainloop()
