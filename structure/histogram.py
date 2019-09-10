#!/usr/bin/env python

def makeHistogram( gradeList ) :

	# Create a 10 element histogram.
	histogram = [0] * 10

	# Count the number of each grade.
	i = 0
	while i < len(gradeList):
		grade = gradeList[ i ] / 10     
		histogram[ grade ] = histogram[ grade ] + 1
		i = i + 1

	# Return the histogram.
	return histogram

gradeList = [ 56, 38, 90, 86, 78, 49, 88 ]
print(makeHistogram(gradeList))

