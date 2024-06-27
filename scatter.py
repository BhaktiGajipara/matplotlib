import matplotlib.pyplot as pl
import numpy as np

# use the scatter() function to draw a scatter plot
# scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, 
# and one for values on the y-axis:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

pl.scatter(x,y)
pl.show()

# Compare Plots
#  set your own color for each scatter plot with the color or the c argument

# day 1, the age and speed of 15 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
pl.scatter(x,y,color = 'red')

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
pl.scatter(x,y,color = 'green')

pl.show()

# Color Each Dot

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

pl.scatter(x, y, c=colors)
pl.show()

# can include the colormap in the drawing by including the plt.colorbar() statement
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
pl.scatter(x, y, c=colors, cmap='viridis')
pl.colorbar()
pl.show()

# Size   //can change the size of the dots with the s argument
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
pl.scatter(x,y,s=sizes)
pl.show()

# Alpha   //can adjust the transparency of the dots with the alpha argument
pl.scatter(x,y,s=sizes,alpha= 0.5)
pl.show()
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# Combine Color Size and Alpha

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

pl.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
pl.colorbar()
pl.show()