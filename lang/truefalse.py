#!/usr/bin/env python

print(bool(''))
# False
print(bool(' '))
# True
print(bool(0))
# False
print(bool("0"))
# True
print(4==4)
# True
print(4=="4")
# False
print(4==4.0)
# True
print(22/7)
# 3
print(22/7.0)
# 3.1428571428571428
print(4 is 4)
# True
print(4 is 4.0)
# False
print("a" is "a")
# True
print("a" is str("a"))
# True

# Now the monkey business
True = -1
print(True)

print(12 == 12)

True == -1

