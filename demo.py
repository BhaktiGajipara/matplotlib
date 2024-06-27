import matplotlib
import matplotlib.pyplot as pl
import numpy as np

# print(matplotlib.__version__)
# Draw a line in a diagram from position (0,0) to position (6,250):

xpoints = np.array([0,6])
ypoints = np.array([0,250])
pl.plot(xpoints,ypoints)
pl.show()

# The plot() function is used to draw points (markers) in a diagram
# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

pl.plot(xpoints,ypoints,"o")
pl.show()

# Multiple Points
# You can plot as many points as you like, just make sure you have the same number of points in both axis

xp = np.array([1,4,5,7])
yp = np.array([3,8,1,10])
pl.plot(xp,yp)
pl.show()

# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points
pl.plot(yp)
pl.show()
