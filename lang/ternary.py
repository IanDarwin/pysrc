#!/usr/bin/env python3

# Equivalent of C/C++/Java ternary operator

list = [0,1,2]

i = 2

# Other languages:
# value = i < len(list) ? list[i] : null;
value = list[i] if i < len(list) else None
print(value)


