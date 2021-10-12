# import tkinder
from tkinter import *
# create the root window
root = Tk()
# everything else is widget
# create button


def handleClick():
    myLabel = Label(root, text="Button Clicked")
    myLabel.pack()


myBtn = Button(root, text="Button", fg="white", bg="black",
               padx=40, pady=40, command=handleClick)
myBtn.pack()
root.mainloop()
