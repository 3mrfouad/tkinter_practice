# import tkinder
from tkinter import *
# create the root window
root = Tk()
# everything else is widget

# create a label that goest into the window
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "Hello Grid")
# shoving it into the root window
myLabel1.grid(row = 0, column =0)
myLabel2.grid(row = 1, column =5)
# create event loop to monitor the continus changes
root.mainloop()
