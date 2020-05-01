#!/usr/bin/env python

# Write some lines to a file (Unix filesystem)
# After running, note that the lines are written
# without any newline characters(!), for a sort
# of symmetry with the equally-oddball readlines().

outfile = open("/tmp/xxx", 'w') 
lines = ['Hello', "Goodbye"]
outfile.writelines(lines);
outfile.close()
