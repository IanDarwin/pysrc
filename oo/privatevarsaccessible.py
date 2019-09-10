#!/usr/bin/env python

# see if private vars are accessible

class X:
	__val = 'base'

x = X()

print(dir(x))

mesg = 'belong to us'

print('All your %ss' % x._X__val, 'are', mesg, "!")
