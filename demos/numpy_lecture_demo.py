"""
if there is a problem with this line:
    do Command+shift+p or Ctrl+shift+p
    search Python: Select Interpreter
    select the 'base' or conda environment
"""
import numpy as np

# add two arrays and add two lists
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 4, 6])

print(f'adding two arrays: {arr1+arr2}' )

# sum of numbers

def loopSum():
    """
    Takes the sum of the numbers 0 to 100 with a loop
    """
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    return sum

loopSum()

def arraySum():
    """
    Takes the sum of the numbers 0 to 100 user Numpy
    """
    listOf100 = np.arange(1, 101)
    return np.sum(listOf100)

arraySum()

# slicing

def lastTwo(myarr):
    """
    Returns the last two columns of the array
    Try to make it work for any input array!
    >>> arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    >>> lastTwo(arr)
    array([[2, 3],
           [5, 6],
           [8, 9]])
    """
    # other solutions: return myarr[:, -2:], return myarr[:, 1:]
    return myarr[:, [1, 2]]

def everyOther(way, myarr):
    """
    Returns every other row or column depending on input for way
    >>> arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    >>> everyOther("row", arr)
    array([[1, 2, 3],
           [7, 8, 9]])
    >>> everyOther("column", arr)
    array([[1, 3],
           [4, 6],
           [7, 9]])
    """
    if way == 'row':
        return myarr[0:len(myarr):2] 
    elif way == 'column':
        return myarr[:, 0:len(myarr):2]
    else:
        return f'Unsupported input! Try again.' 

# useful functions

print(f'I can make an array of zeros: {np.zeros(4)}')
print(f'I can make an array of random numbers: {np.random.random(5)}')

