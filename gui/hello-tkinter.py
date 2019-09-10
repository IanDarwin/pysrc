#!/usr/bin/env python

from Tkinter import Tk,Button,Label,Entry

global field

rootWindow = Tk()

label = Label(rootWindow, text="Hello, world!")
label.pack()

def handler(*args):
	global field
	print("You said", field.get())

field = Entry(rootWindow)
field.pack()
field.bind('<Key-Return>', handler)

button = Button(rootWindow, text='Go!', command=handler);
button.pack()

rootWindow.mainloop()
