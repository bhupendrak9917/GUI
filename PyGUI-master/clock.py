from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
def time():
    string = strftime("%H:%M:%S:%p")
    label.config(text=string)
    label.after(1000,time)
label = Label(root, font=("d%-digital",40),background="black",foreground="blue")
label.pack(anchor="center")
time()
mainloop()