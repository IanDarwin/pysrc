import itertools

# Simply chain together non-addable collections
# [...] + (...) gives a TypeError
print([x for x in itertools.chain([1, 2, 3], ('a', 'b', 'c'))])

# Iterate over a list, dropping values that are < 0
print([x for x in itertools.dropwhile(
	lambda x: x<0, # predicate
	[-1, -2, -1, 0, 3, 4])])

# The latter can be done more simply with a comprehension though
print([x for x in [-1, -2, -1, 0, 3, 4] if not x < 0])
