from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x300")
def msg():
    messagebox.showwarning("Warning", " there is a virus found")
button = Button(root, text="scan for virus",command = msg)
button.place(x=40 , y=80)
root.mainloop()