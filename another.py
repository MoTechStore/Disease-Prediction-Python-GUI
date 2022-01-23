from tkinter import *

root = Tk()
photo = PhotoImage(file="m.png")
w = Label(root, image=photo)
w.pack()
root.mainloop()