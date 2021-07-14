#!/usr/bin/env python3

'''
Show formatting a price and tax using
different format orders in different locales.
'''
price = 123.45
tax_rate = 0.07
en_str = 'price ${0:6.2f}, tax @ {1}, total ${2:6.2f}';
es_str = "total ${2:6.2f} (precio ${0:6.2f}, impuesta @ {1})"
string = en_str
print(string.format(price, tax_rate, (1+tax_rate) * price))
string = es_str
print(string.format(price, tax_rate, (1+tax_rate) * price))
