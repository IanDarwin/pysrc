''' 
	Demonstrates reading a SAS save file into Python using Pandas
    This assumes you have install the py3-pandas package or done pip install pandas or similar.
	Pyreadstat gives a bit more flexibility but requires you to download the file.
	Plus, it's just one more dependency to import. :-)
	Adapted from https://www.marsja.se/how-to-read-sas-files-in-python-with-pandas
'''

import pandas as pd

url = 'http://www.principlesofeconometrics.com/sas/airline.sas7bdat'

data = pd.read_sas(url)
print(data.head())

# import pyreadstat as pyr
# cols = 'Year','R','W'
# data2 = pyr.read_sas7bdat('airline.sas7bdat', usecols=cols)
# print(data2.tail())
