# -*- coding: utf-8 -*-
"""
LOOPS! 

Loops help you iterate code over a period of time. Instead of 
writing numerous lines of code, using a loop saves lots of 
time and shortens your code.

Types of Loops:

While Loops

While loops repeat a series of statements until a condition 
is met. Some while loops may require an outside counter to keep 
track of what's happening in the while loop or just as a variable.

        
For example, run the file to see what outputs:
"""

"""
Syntax:
    while [condition]:
        do this
"""

count = 0
while count < 4:
    print(count)
    count += 1

"""
For Loops

For loops are best used to iterate over a list or array (but 
I personally prefer to use them in any case I can :3)
"""

"""
Syntax:
    for [iteration] in [sequence]:
        do this
"""

# run the file
for i in range(0, 10):
    print(i)

"""
Conditional statements (if and else) are often implemented 
in loops. An example is shown below:
"""

for i in range(1, 50):
    if i % 10 != 0:
        print(i)

"""
Practice Problems!

Now it's your turn! Try these problems ranging from easy to hard :)

1. Print every element in the provided list.
"""

list = ['megan', 'charlie', 'mahum', 'pranathi', 'mira', 'jonah', 'josh', 'brianna']
for element in list:
    print(element)
    
'alternate solution'
i = 0
while i < len(list):
    print(list[i])
    i += 1

"""
2. Write a loop that prints out the sum of all the numbers from 1 through 10 (including 10).
Hint: you may need an outside variable :o
"""

c = 0
for i in range(1, 11):
    c += i

print(c)

'alternate solution'
values = 0
add = 0
while values < 10:
    values += 1
    add += values
print(add)

"""
3. Find the sum of the digits in the number 21617 
Ex. sum of 123 is 6
"""

n = 21617
add = 0
while n > 0:
    add += n % 10
    n //= 10
print(add)

"""
4. Find the factorial of a number, 10, but stop when you get to 3. 
Essentially, compute 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3
"""

top = 10
bottom = 3
factorial = 1
while bottom <= 10:
    factorial *= bottom
    bottom += 1
print(factorial)

'alternate solution'
t = 10
b = 3
f = 1
for i in range(b, t + 1):
    f *= i
print(f)
