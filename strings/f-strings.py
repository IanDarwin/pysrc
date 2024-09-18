# f-strings support interpolation of values

import math

r = 2
print(f'Area = {math.pi * r * r}')
# should print "Area = 12.566370614359172"

# Can also use printf format codes:
print(f'Area = {math.pi * r * r:6.4f}')
