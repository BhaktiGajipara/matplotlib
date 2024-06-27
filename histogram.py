import matplotlib.pyplot as pl
import numpy as np

# A histogram is a graph showing frequency distributions
# use the hist() function to create histograms
# simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, 
# and the standard deviation is 10.

x = np.random.normal(170,10,250)
pl.hist(x)
pl.show()