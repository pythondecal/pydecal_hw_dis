# Preamble

import numpy as np

"""
Numpy Review - Python DeCal

In this notebook we will give you a few practice problems involving `numpy` 
to strengthen your skills. Feel free to try as many as you want. We will 
organize these as three different problems of varying difficulty. The first 
ones will be the easiest and the the last ones will be a difficult challenge.

Question I: Fundamentals

Let's get back to the basics before we try anything fancy! There will be a 
few subparts but they should be fairly quick:

A) Creating Arrays

Write some code to generate a 1D array of 1000 evenly spaced numbers from 
0 to 2pi. Then create a second array where each value in the array is 
double that of the previous array (call these `x1` and `x2` respectively)
"""

# YOUR CODE HERE

"""
B) Take the Mean, Median, and Standard Deviation

Take the mean, median, and standard deviation of `x1` and `x2` using `numpy`
"""

# YOUR CODE HERE

"""
C) Create a 2D Array

Create a 2D array called `filter` of shape `(1000, 1000)` populated with only 
0's. Then set the first quadrant of this equal to 1's using index slicing. 
We will use this later. 
Hint (The first 500 indices in each axis is what we want to set = 1)
"""

# YOUR CODE HERE

"""
D)  Let's Create a Boolean Filter

Use the `filter` array of $1$'s and $0$'s to create a boolean array. 
To do this, you might consider googling how to change the `dtype` of a 
`numpy` array
"""

# YOUR CODE HERE


"""
Question III: Axis Wise Operations

A common problem we face when using `numpy` arrays is taking averages 
across a certain axis. Let's say for example we have 1D array of data 
that shows the brightness of an exoplanet over time, this array represents 
1 observation of the exoplanet. When Astronomers want to really make sure 
the signal is valid, we have to observe it multiple times. In this example 
we load in a numpy array of size `(100, 1000)` where the 0th axis 
represents each observation and the 1st axis represents the brightness as 
a function of time. Load in the Data and take a look at the shape 
(`data.shape`)
"""
# This line loads some data, make sure the file is in the same location as 
# this one!
exoplanet_data = np.loadtxt('exoplanet_observations.csv', delimiter=',') 

# Makes an evenly spaced out array of 1000 elements with the numbers 0 to 100
time = np.linspace(0, 100, 1000) #x-axis in units of days

"""### A) Averaging the Lightcurve

Take the average lightcurve of all the observations. Remember you can compute 
the mean across only a single axis. You should be left with a 1D array of 
length = 1000. Call this new array `avg_lc`
"""

# YOUR CODE HERE

"""
B) Making Data Cuts

Now we are only interested in the dip of the light because that corresponds 
to the planet crossing in front of the star in our line of sight. This is a 
pretty useful tool astronomers use, we call it the "transit method". With 
this astronomers can learn the mass and size of the planet! Your colleague 
approaches you and says "Hey, could you isolate the signal to only the transit 
dip?"... Let's do that in this problem. Filter the average lightcurve array so 
that it only includes values where the brightness is less than 1 (the default 
brightness when the planet is not in front of the star.)
"""

# YOUR CODE HERE