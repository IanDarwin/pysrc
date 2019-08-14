#!/usr/bin/env python

import Gnuplot

plotter = Gnuplot.Gnuplot(persist = 1) 
plotter('set data style lines')

# plot x^2 : x for range 0..20
rd = range(20+1)
data = [(r,r*r) for r in rd]
print data
plotter.plot(data)
data = [(r,r/4) for f in rd]
plotter.addplot(data)
