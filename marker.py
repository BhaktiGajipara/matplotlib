import matplotlib.pyplot as pl
import numpy as np

# Markers
# You can use the keyword argument marker to emphasize each point with a specified marker:

ypoints = np.array([3,8,1,10])
pl.plot(ypoints, marker = '*')
pl.show()

# there are other also like d,>,^,.,(,),a,p and many more

# Format Strings fmt
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color
# "-" -solid line     ":" -doted line  "--" -dash line  "-." -dash dotted line
pl.plot(ypoints,'o:m')
pl.show()
pl.plot(ypoints,'o-c')
pl.show()
pl.plot(ypoints,'o--k')
pl.show()
pl.plot(ypoints,'o-.g')
pl.show()

# Marker Size   //markersize or the shorter version, ms to set the size of the markers
pl.plot(ypoints, marker = '*',ms = 20)
pl.show()

# Marker Color   //markeredgecolor or the shorter mec to set the color of the edge of the markers
pl.plot(ypoints, marker = '*',ms = 20,mec = 'm')
pl.show()

# use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
pl.plot(ypoints, marker = '*',ms = 20,mfc = 'm')
pl.show()

# Use both the mec and mfc arguments to color the entire marker:
pl.plot(ypoints, marker = '*',ms = 20,mfc = 'm',mec = "m")
pl.show()