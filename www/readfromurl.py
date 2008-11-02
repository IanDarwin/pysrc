#!/usr/bin/env python

import urllib

# define a URL path
url = "http://www.darwinsys.com/"

file = urllib.urlopen(url)

text = file.read()

print text
