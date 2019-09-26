#!/usr/bin/env python

# Shows various ways of splitting a sequence such as a string.
# Also shows an alternate way of printing: list unpacking with
# printf-style format codes instead of {name}
# And yes, we could have just used string.split() :-)

name = "Ian Darwin"

first = name[0:3]
last = name[4:]
print("Name split by slice: %s, %s" % (last, first))

sp = name.find(' ')
first = name[0:sp]
last =  name[sp+1:]
print("Name split by find:  %s, %s" % (last, first))

print("Sliced and diced:", name[4:-2:2])

print("Backwards", name[::-1])
