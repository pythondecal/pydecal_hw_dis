import numpy as np

# PROBLEM 1: PUT IT IN REVERSE TERRY!

"""
    Make a function that takes in an array. Reshape the array 
    so that it becomes a square matrix. Finally reverse the
    multi-dimensional array and return it.

    EXTRA think about what kinds of arrays can be inputted
"""

def reverseArray(arr):
    """
     >>> np.random.seed(12345)
    >>> myArr = np.random.randint(0, 10, size=(9))
    >>> myArr
    array([2, 5, 1, 4, 9, 5, 2, 1, 6])
    >>> reverseArray(myArr)
    array([[6, 1, 2],
           [5, 9, 4],
           [1, 5, 2]]

    >>> badLength = np.random.random(6)
    >>> reverseArray(badLength)
    Array length or dimension is not supported. Please try again.

    >>> wrongDim = np.random.random(4)
    >>> reverseArray(np.reshape(wrongDim, (2, 2)))
    Array length or dimension is not supported. Please try again.'
    """
    "YOUR CODE HERE"



# PROBLEM 2: IT'S NICE TO BE DIFFERENT

"""
    Given an array, return its sorted version with only the unique 
    elements, along with the count for each value.

    P.S. There is an easy way and a hard way xp
"""

def uniqueCounts(myArr):
    """
    >>> arr = np.array([10, 2, 5, 10, 8, 2, 8, 9])
    >>> uniqueCounts(arr)
    (array([ 2, 5,  8,  9, 10]), array([2, 1, 2, 1, 2]))
    """
    "YOUR CODE HERE"



# PROBLEM 3: NO FAKES HERE

"""
    Given a multidimensional array, find the mean along the columns.
    Then, replace each value that is less than the mean with the 
    mean of that column.
"""

def condtionedArr(myArr):
    """
    >>> np.random.seed(12345)
    >>> newArr = np.random.randint(0, 50, size=(4, 3))
    >>> newArr
    array([[34, 37, 29],
           [ 1, 36, 41],
           [37, 34, 29],
           [ 1, 49, 14]])
    >>> conditionedArr(newArr)
    array([[34, 39, 29],
           [18, 39, 41],
           [37, 39, 29],
           [18, 49, 28]])
    """
    "YOUR CODE HERE"



# PROBLEM 4: WHERE IS YOUR PLACE IN LIFE?

"""
    You are given a sorted array and an input or multiple inputs. 
    Your job is to find the index or indices where you could
    place the input so that the array is still sorted.
"""

def sortAndInsert(arr, inputVal):
    """
    >>> sortArr = [1, 2, 3, 4, 7]
    >>> sortAndInsert(sortArr, 5)
    4

    >>> sortedArr = [1, 3, 7, 20, 32]
    >>> sortAndInsert(sortArr, [5, 18, 24, 26])
    array([4, 5, 5, 5])
    """
    "YOUR CODE HERE"