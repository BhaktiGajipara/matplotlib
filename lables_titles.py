import matplotlib.pyplot as pl
import numpy as np

# Create Labels for a Plot
# you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis
# Create a Title for a Plot  //you can use the title() function to set a title for the plot

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
pl.plot(x,y)
pl.title("Sports watch data")
pl.xlabel("Avarage pulse")
pl.ylabel("Calories burn")
pl.show()

# Set Font Properties for Title and Labels
#  use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels
fon1 = {"family":"serif","color":"blue","size":20}
fon2 = {"family":"serif","color":"darkred","size":15}
pl.plot(x,y)
pl.title("Sports watch data",fontdict=fon1)
pl.xlabel("Avarage pulse",fontdict=fon2)
pl.ylabel("Calories burn",fontdict=fon2)
pl.show()

# Position the Title  //use the loc parameter in title() to position the title
pl.plot(x,y)
pl.title("Sports watch data",loc="left")
pl.xlabel("Avarage pulse")
pl.ylabel("Calories burn")
pl.show()