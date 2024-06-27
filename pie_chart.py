import matplotlib.pyplot as pl
import numpy as np

# use the pie() function to draw pie charts
y = np.array([35, 25, 25, 15])
pl.pie(y)
pl.show()

# Labels //Add labels to the pie chart with the labels parameter
my_lable = ["custerd apple","cherry","mango","apple"]
pl.pie(y,labels=my_lable)
pl.show()

# Start Angle
# default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
# The startangle parameter is defined with an angle in degres, default angle is 0
pl.pie(y,labels=my_lable,startangle=90)
pl.show()

# Explode
myexplode = [0.2, 0, 0, 0]
pl.pie(y,labels=my_lable,explode=myexplode)
pl.show()

# Shadow  //Add a shadow to the pie chart by setting the shadows parameter to True
pl.pie(y,labels=my_lable, explode=myexplode, shadow= True)
pl.show()

# Colors
# Legend  //To add a list of explanation for each wedge, use the legend() function
# Legend With Header  // To add a header to the legend, add the title parameter to the legend function
mycolors = ["black", "hotpink", "b", "#4CAF50"]
pl.pie(y,labels=my_lable, explode=myexplode, shadow= True, colors=mycolors)
pl.legend(title = "Fruits")
pl.show()
