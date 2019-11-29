#!/usr/bin/env python

# pip install tkinter if the next line shows 'unresolved':
from tkinter import Tk,Frame,Button

class HelloButton(object):
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()
            self.button = Button(frame, text="Exit", command=frame.quit)
            self.button.pack()

root = Tk()

prog = HelloButton(root)

root.mainloop()
