#!/usr/bin/env python

# List unpacking - what CS folks call "destructuring assignment"

a, b = [10, 20];

print(a)
# output: 10

print(b)
# output: 20

a, b, *rest = [10, 20, 30, 40, 50];

print(rest);
# expected output: [30,40,50]

