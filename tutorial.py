# import tkinder
from tkinter import *
# create the root window
root = Tk()
# everything else is widget
def handleClick():
    myLabel = Label(root, text=f"Hello {e.get()}")
    myLabel.pack()
  
# input box
myLabel = Label(root, text="Enter your name: ")
myLabel.pack()

e = Entry(root, width=50, bg="black", fg="white", borderwidth=3)
e.insert(0, "Your Name:") # default text not a placeholder
e.pack()

myBtn = Button(root, text="Ok", fg="white", bg="black",
               padx=40, pady=40, command=handleClick)
myBtn.pack()
root.mainloop()
