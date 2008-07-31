name = "Ian Darwin"

first = name[0:3]
last = name[4:]
print "Name sliced by magic: %s, %s" %(last, first)

sp = name.find(' ')
first =name[0:sp]
last = name[sp+1:]
print "Name sliced by find:  %s, %s" %(last, first)
