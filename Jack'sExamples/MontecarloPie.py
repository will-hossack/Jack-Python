"""
Simple program to approximate PI using Montecarlo methods. Imagaine we could fire a paint gun at a circle of radius r
inscribed in a rectangle of side length r. By randomly firing our gun across the square some shots would land in the
circle and others wouldn't. We could then take the ratio of shots that landed inside the circle and those that just
landed in the square (the toatal number of shots). By taking enough shots we get that
NumberShotsInsideCircle/TotalNumberShots = areaCircle/areaSquare = Pi*r*r/(2r*2r)
rearranging we get Pi = 4* NumberShotsInsideCircle/TotalNumberShots

This is the method the following program implements
"""
from random import random
# total number of random points we will create
totalNumberPoints = 10000000
# number of points that land inside circle, initially 0
numberPointsInCircle = 0
# start randomly distributing points
for i in range(totalNumberPoints):
    # the final formula is independent of the radius of the circle, so we will just distribute random points between
    # (0,1). As long as the random numbers are generate to a good number of significant figures this wont be a problem
    x,y = random(),random()
    # check to see if the point is in our circle
    if (x*x)+(y*y) < 1:
        # if it is increment out counter
        numberPointsInCircle +=1

# apply the formula above and print PI

Pi = numberPointsInCircle/totalNumberPoints*4
print("Pi = " + str(Pi))


