import matplotlib.pyplot as pl
import numpy as np

# use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
# "dotted //:","dashed//--","solid//-","dashdot//-.","None//"or"""
ypoints = np.array([3,8,1,10])
pl.plot(ypoints, linestyle = 'dotted')
pl.show()

# Line Color   //use the keyword argument color or the shorter c to set the color of the line
pl.plot(ypoints, c = 'r')
pl.show()

# Line Width //You can use the keyword argument linewidth or the shorter lw to change the width of the line
pl.plot(ypoints, lw = 20.6)
pl.show()

# Multiple Lines //You can plot as many lines as you like by simply adding more plt.plot() functions
y2points = np.array([6, 2, 7, 11])
pl.plot(ypoints)
pl.plot(y2points)
pl.show()

# Draw two lines by specifiyng the x- and y-point values for both lines:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

pl.plot(x1,y1,x2,y2)
pl.show()

