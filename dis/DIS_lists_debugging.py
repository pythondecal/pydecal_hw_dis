# Lists and Debugging Discussion

"""
Helpful Functions for Dictionaries:
Suppose you made a dictionary named dict
    dict.get(key) -> outputs the value at key
    dict.keys() -> outs a list of all keys
    dict.values() -> outputs a list of all values
    dict.items() -> outputs a list of tuples for each key value pair
"""

# Problem 1: Shopping Cart Analyzer
"""
You are given two lists representing a customer's shopping cart and the 
corresponding prices of the items in the cart. Additionally, you have a 
dictionary that maps item names to their discount percentages. Write a 
function in Python that calculates the total cost of the customer's shopping 
cart, taking into account any applicable discounts.
"""
#Example:

# Input
cart_items = ['apple', 'banana', 'orange', 'milk']
item_prices = [1.2, 0.9, 1.0, 2.5]
discounts = {'apple': 0.1, 'banana': 0.05}

# Output
# 4.42

"YOUR CODE HERE"

# Problem 2: Grouping Dictionary Elements
"""
You are given a list of dictionaries, each containing information about a 
person, including their name and age. Write a function in Python that groups
the people by age, returning a dictionary where the keys are the ages, and the 
values are lists of names belonging to that age group.
"""
# Example:
# Input
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 25}
]

# Output: {30: ['Alice', 'Charlie'], 25: ['Bob', 'David']}

"YOUR CODE HERE"

# Problem 3: Most Frequent Element

"""
Write a Python function that takes a list as input and returns 
the most frequently occurring element along with its frequency. 
If there are multiple elements with the same highest frequency, 
return the one that appears first in the list.
"""

# Example:
# Input
numbers = [2, 3, 5, 2, 8, 2, 5, 6, 3, 2, 9, 5]

# Output: (2, 4)

"YOUR CODE HERE"



""" The rest of the discussion is taken from or inspired by the CS61A 
    debugging practice worksheet from Spring 2022 """

# PROBLEM 4
""" You're writing your own implementation of the map function which 
takes in a one-argument function and applies it to every element in a list
and returns a new list. However, you are running into some bugs.

The is what you expect to happen:
>>> def double(x):
        return x*2
>>> lst = [1, 2, 3]
>>> my_map(double, lst)
[2, 4, 6]

This is the code you've written so far:
    1 def my_map(func, seq):
    2   res = []
    3   for i in seq:
    4       curr = func(seq[i])
    5       res.append(curr)
    6   return res
    
This is the error you get:
    >>> my_map(double, lst)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/Users/yourname/pydecal/my_map.py", line 4, in my_map
            curr = func(seq[i])
    IndexError: list index out of range"""

 # PART 1
""" What line is your error on? """
print("The error is on line: ", "YOUR ANSWER HERE")

# PART 2
""" Rewrite that line to correct the error
    Please keep the code in quotes!"""
print("The line should be: ", "YOUR CODE HERE")



# PROBLEM 2

""" 
Some people on the internet have run into problems with their code.
It's your job to help them figure it out!

Here is the code:

    1 percentages = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
    2 max_score = 300
    3
    4 scores = [[int(percent * max_score) for percent in percentages]
    5
    6 print('Scores corresponding to the given percentages, on a scale out of 300:')
    7 print(scores)
    
The expected output is:
    Scores corresponding to the given percentages, on a scale out of 300:
    [300, 270, 240, 210, 180, 150, 120, 90, 60, 30, 0]
    
But instead you get:
    File '/Users/yourname/pydecal/scores.py;, line 6
        print('Scores corresponding to the given percentages, on a scale out of 300:')
        ^
    SyntaxError: invalid syntax
"""

# PART 1
""" What line is your error on? """
print("The error is on line: ", "YOUR ANSWER HERE")

# PART 2
""" Rewrite that line to correct the error
    Please keep the code in quotes!"""
print("The line should be: ", "YOUR CODE HERE")


# PROBLEM 3

"""
You wrote some code for class but you have run into an unexpected output.
You are trying to calculate the bmi based on data you have. Somehow, the
calculated BMI always seems to be the same no matter what data you input
into it. Here's what you have:

    1 patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
    2
    3 def calculate_bmi(weight, height):
    4    return weight / (height ** 2)
    5
    6 for patient in patients:
    7    weight, height = patients[0]
    8    bmi = calculate_bmi(height, weight)
    9    print(f'Patient's BMI is: {bmi}')

The output you get is:
    Patient's BMI is: 0.000367
    Patient's BMI is: 0.000367
    Patient's BMI is: 0.000367

Modify the code so that it works as intended.
** Try to only change 2 lines! **
"""

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

"YOUR CODE HERE"
