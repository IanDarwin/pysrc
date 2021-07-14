t=(1,2,3)
# If you uncomment the following line - change t from tuple to list - the
# dictionary creation will crash with "TypeError: unhashable type: 'list':
# t=[1,2,3]
d={t:'hello', 1:'goodbye'}
print(d)

