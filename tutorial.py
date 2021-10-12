# import tkinder
from tkinter import *
# create the root window
root = Tk()
# everything else is widget

# create a label that goest into the window
myLabel = Label(root, text = "Hello World!")
# shoving it into the root window
myLabel.pack()
# create event loop to monitor the continus changes
root.mainloop()
