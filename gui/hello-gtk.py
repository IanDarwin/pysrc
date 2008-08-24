#!/usr/bin/env python

# Original retrieved from "http://wiki.openmoko.org/wiki/Python"

import gtk

# create a (nonvisible) window 
w = gtk.Window()

# create a button (not yet on any window)
b = gtk.Button('Hello')

# put the button on the window
w.add(b)

# create a silly callback function
def hello(target):
  print 'Goodbye cruel world'
  exit()

# make the button call the callback when pressed('clicked')
b.connect('clicked', hello)

# make the window display
w.show_all()

# start processing screen events
gtk.main()



