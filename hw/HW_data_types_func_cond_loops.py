
#Homework 3: Data Types, Functions, Conditionals, and Loops



""" ### Problem 1: Power of a Number:
Write a function to compute the value of x raised to the power y (x^y) 
without using the built-in pow or ** operator.
"""

def power(input, power):
  "YOUR CODE HERE"



"""### Problem 2: Minimum and Maximum
Write a function that takes a list of numbers as input and returns the 
minimum and maximum values in the list as a tuple.
"""

def minandmax(list1):
  "YOUR CODE HERE"



"""### Problem 3: Check Leap Year
Write a function that takes a year as input and returns True if it's a 
leap year, and False otherwise. A leap year is divisible by 4 but not divisible 
by 100 unless it is also divisible by 400.
"""

def leapYear(year):
  "YOUR CODE HERE"



"""### Problem 4: Calculate BMI (Body Mass Index):
Write a function that takes a person's weight (in kilograms) and height 
(in meters) as input and returns their BMI.
"""

def calculate_bmi(weight, height):
    "YOUR CODE HERE"



"""### Problem 5: Rotating Digits
Implement a function called rotate_digits that takes an integer n as input and 
rotates its digits to the right by one position. For example, given the input 12345, 
the function should return 51234. You may *not* convert the input to a string but 
you can use properties of a string in your answer.

**Hint:** Use modulus (%) and floor division (//). For example, 12345 % 10 = 5 and 
12345 // 10 = 1234
"""

def rotate_digits(digits):
  "YOUR CODE HERE"





### For questions #6-10, write the solution with a for-loop and a while-loop.
# If it is not possible to write it with a for-loop or while-loop, detail why.

"""Problem 6: Maximum
Given a list of numbers, find the maximum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMax(lis):
   "YOUR CODE HERE"




"""Problem 7: Minimum
Given a list of numbers, find the minimum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMin(lis):
   "YOUR CODE HERE"



"""Problem 8: The Product
Given a list of numbers, calculate the product of all the numbers.
"""

def product(numList):
   "YOUR CODE HERE"



"""Problem 9: Vowels
Given a string, count the number of vowels in it using a for loop.

"""

string1 = "pneumonoultramicroscopicsilicovolcanoconiosis"

def countVowels(str):
   "YOUR CODE HERE"



"""Problem 10: Sum of Digits (Digital Root):
Given an integer, return the sum of its digits (also known as the digital 
root) For example, if the input is 12345, the output should be 15 
(1 + 2 + 3 + 4 + 5).

**Hint:** Refer to #5!

"""

# For this question, it is harder to do it as a for-loop as there is no 
# way of keeping track of all the digits.
# So, only a while-loop solution is necessary.

def sumDigits(num):
   "YOUR CODE HERE"