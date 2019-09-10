import itertools
print([x for x in itertools.chain([1, 2, 3], ('a', 'b', 'c'))])

print([x for x in itertools.dropwhile()
	lambda x: x<0, # predicate
	[-1, -2, -1, 0, 3, 4])]

