import matplotlib.pyplot as pl
import numpy as np

# take the keyword argument color to set the color of the bars

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

pl.bar(x,y,color = "pink")
pl.show()

# Horizontal Bars   //use the barh() function:
pl.barh(x,y)
pl.show()

# Bar Width  //takes the keyword argument width to set the width of the bars
pl.bar(x,y,width=0.1)
pl.show()

# barh() takes the keyword argument height to set the height of the bars
pl.barh(x,y,height= 0.1)
pl.show()