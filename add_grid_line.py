import matplotlib.pyplot as pl
import numpy as np

# Add Grid Lines to a Plot
# you can use the grid() function to add grid lines to the plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
pl.plot(x,y)
pl.title("Sports watch data")
pl.xlabel("Avarage pulse")
pl.ylabel("Calories burn")
pl.grid()
pl.show()

# Specify Which Grid Lines to Display
# use the axis parameter in the grid() function to specify which grid lines to display
pl.plot(x,y)
pl.title("Sports watch data")
pl.xlabel("Avarage pulse")
pl.ylabel("Calories burn")
pl.grid(axis="x")
pl.show()

# Set Line Properties for the Grid
#  grid(color = 'color', linestyle = 'linestyle', linewidth = number)
pl.plot(x,y)
pl.title("Sports watch data")
pl.xlabel("Avarage pulse")
pl.ylabel("Calories burn")
pl.grid(color = "green", ls = "--", lw = 0.5 )
pl.show()