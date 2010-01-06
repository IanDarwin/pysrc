#!/usr/bin/env python

# read lines from a kitsRus "K145" temperature sensor

import sys
import time

def save(temp):
	f = open("temperature.txt", "w")
	m = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	f.write("%04.2f %s\n" % (float(temp), m))
	f.close()


while (True):
	line = sys.stdin.readline();
	if (line.startswith("1")):
		temp = line.split()[1]
		save(temp)
	else:
		print "REJECT: " + line
