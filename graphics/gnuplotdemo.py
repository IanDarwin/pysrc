import Gnuplot

plotter = Gnuplot.Gnuplot(persist = 1) 

plotter('set data style lines')

# plot x^2 : x for range 0..20
rd = range(20+1)
data = [(r,r*r) for r in rd]
plotter.plot(data)
