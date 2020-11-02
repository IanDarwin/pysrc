#!/usr/bin/env python

# You can do set operations on a dict_keys object:

dict1 = { 'Carpenter' : "Bob",  'Security Guard' : "Sally" , 'Supervisor': 'Harr'}
dict2 = { "Supervisor": 'Bob', 'Aunt': 'Sally', 'Cousin': 'Robin'}

print("Occupations in both groups:")
print(dict1.keys() & dict2.keys())

