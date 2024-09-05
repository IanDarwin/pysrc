#!/usr/bin/env python3

data = [ 2, 4, 6, 8 ]

it = iter(data)

print(dir(it))
print((it.__iter__))
print((it.__next__))

print(f'First call to next = {next(it)}')
for i in it:
	print(i)
