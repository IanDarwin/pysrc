#!/usr/bin/env python

# Demo writing your own exception

class MyException(Exception):
	pass

raise MyException("Bad Input", 42)
