from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("products")
window.geometry("400x400")
n1 = float(input("enter a number:"))
n2 = float(input("enter another number:"))
product = n1 * n2
messagebox.showinfo("product", f"the product of {n1} and {n2} is {product}")
window.mainloop()