# NUMPY ARRAYS HOMEWORK

# DON'T USE FOR LOOPS!!!!!

"""
    if there is a problem with this line:
    do Command+shift+p or Ctrl+shift+p
    search Python: Select Interpreter
    select the 'base' or conda environment
"""
import numpy as np

# remember to run this line in the terminal to run doctests
# python3 -m doctest <file name>

# PROBLEM 1: HEY TWIN

"""
Given an array, find the rows where all the values are equal. 
"""
def findEqual(arr):
    """
    >>> arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
    >>> findEqual(arr)
    array([[1, 1, 1],
           [2, 2, 2]])
    """
    "YOUR CODE HERE"


# PROBLEM 2: CHECKERS

"""
Create an 8x8 array with a checkerboard pattern of 
zeros and ones using a slicing + striding approach
"""

def checkerboard():
    """
    >>> checkerboard()
    array([[1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1]])
    """
    "YOUR CODE HERE"


# PROBLEM 3: I NEED SOME SPACE

"""
Given an array of strings, return an array where
each letter in each string is separated by a space.
"""

def spaceBetween(stringArr):
    """
    >>> myarr = np.array(['python', 'is', 'cool!'])
    >>> spaceBetween(myarr)
    array(['p y t h o n', 'i s', 'c o o l !'], dtype='<U11')
    """
    "YOUR CODE HERE"


# PROBLEM 4: EVERYTHING IS IN ORDER

"""
Given a multidimensional matrix, sort the matrix along the
columns.
"""

def sorting(bigMatrix):
    """
    >>> np.random.seed(12345)
    >>> a = np.random.randint(1,50, (4, 5))
    >>> a
    array([[35, 38, 30,  2, 37],
           [42, 38, 35, 30,  2],
           [15, 42, 28, 17, 10],
           [12, 14, 11, 18, 19]])

    >>> sorting(a)
    array([[12, 14, 11,  2,  2],
           [15, 38, 28, 17, 10],
           [35, 38, 30, 18, 19],
           [42, 42, 35, 30, 37]])
    """
    "YOUR CODE HERE"
