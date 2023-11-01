#!/usr/bin/env python

text = "Once, upon a midnight dreary, while I pondered, weak and weary, over many a quaint and curious volume of forgotten lore..."

w_words = [ w for w in text.split() if w.startswith('w') ]

print(w_words)
