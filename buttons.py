from tkinter import *
window = Tk()
window.title("sample frame")
window.geometry("300x200")
border_effects = ["flat", "raised", "sunken", "groove", "ridge"]
for r in border_effects:
    frame = Frame(master=window, borderwidth=5, relief=r)
    frame.pack(side=LEFT)
    label = Label(master=frame, text=r)
    label.pack()