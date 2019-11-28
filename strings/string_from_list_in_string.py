#!/usr/bin/env python

# find if any of the words in a list is a subsequence of a string

list = ['in','on','an'];

string = "Once upon any time a String walked into a bar..."

if any(tmp in string for tmp in list):
	print("At least one substring matches")

match = next((tmp for tmp in list if tmp in string), False)
print('First match:', match)

matches = [tmp for tmp in list if tmp in string]
print('All matches (including duplicates):', matches)

matches = {tmp for tmp in list if tmp in string}
print('All non-duplicate matches (disregarding order):', matches)

matches = []
for tmp in list:
    if tmp in string and tmp not in matches:
        matches.append(tmp)
print('All non-duplicate matches in order:', matches);
