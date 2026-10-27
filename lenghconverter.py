from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("inches to centimetres")
window.geometry("200x100")
inches = float(input("enter any number in inches: "))
centimetres = inches * 2.54
msg = messagebox.showinfo("Result", f"{inches} inches is equal to {centimetres} centimetres")
window.mainloop()