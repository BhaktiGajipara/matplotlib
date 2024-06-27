import matplotlib.pyplot as pl
import numpy as np

# With the subplot() function you can draw multiple plots in one figure
# subplot() function takes three arguments
# rows and columns, which are represented by the first and second argument.
# // The third argument represents the index of the current plot

# plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

pl.subplot(1,2,1)
pl.plot(x,y)

# plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
pl.subplot(1,2,2)
pl.plot(x,y)

pl.show()

# Draw 2 plots on top of each other
# plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

pl.subplot(2,1,1)
pl.plot(x,y)

# plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
pl.subplot(2,1,2)
pl.plot(x,y)

pl.show()

# You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.
# Title  //add a title to each plot with the title() function
# Super Title  // You can add a title to the entire figure with the suptitle() function:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

pl.subplot(2, 3, 1)
pl.plot(x,y)
pl.title("sales")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

pl.subplot(2, 3, 2)
pl.plot(x,y)
pl.title("income")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

pl.subplot(2, 3, 3)
pl.plot(x,y)
pl.title("xyz")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
pl.title("abcd")

pl.subplot(2, 3, 4)
pl.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

pl.subplot(2, 3, 5)
pl.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

pl.subplot(2, 3, 6)
pl.plot(x,y)

pl.suptitle("My shop")
pl.show()