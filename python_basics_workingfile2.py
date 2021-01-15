# -*- coding: utf-8 -*-
"""
@author: Suresh Reddy Nusi
"""

"""
Python function in any programming language is a sequence of statements in a certain order, 
given a name. When called, those statements are executed. So we don’t have to write the 
code again 
and again for each [type of] data that we want to apply it to. 
This is called code re-usability.
Advantages:
This Python Function help divide a program into modules. This makes the code easier to manage, debug, and scale.
It implements code reuse. Every time you need to execute a sequence of statements, all you need to do is to call the function.
This Python Function allow us to change functionality easily, and different programmers can work on different functions.
"""
def hello():
    print("Hello")
    
hello()

"""
Passing the parameters to the functions
"""
def sum(a,b):
    c=a+b
    print(c)
    
sum(2,3)

"""
passing the parameters and returning the value from the fuction
"""

def sum(a,b):
    c=a+b
    return c

s=sum(5,10)

"""
The above we discussed are the User - defined  functions, apart from this we have
1.Built-in functions
2.Lambda functions
3.Recursion functions

"""


"""
In Python programming, especially when you're dealing with data,
 there are many cases where you want to iterate over list or dict, 
 perform an operation on every element, 
 and then collect all the results in a new list or dict. 
 This can be done with a For Loop, 
 but Python offers a great feature, comprehensions, 
 that lets you write shorter and clearer code that achieves the same effect.
"""
#First we will create a list of squares from 0 to 9.
squares = []

for i in range(10):
    squares.append(i**2)

squares

#The above code can be reduced to one line only using comprehension.
squares = [i**2 for i in range(10)]
squares

#More examples for practice
#Return square of numbers in range o to 20 that are divisible by 3.
squares = [i**2 for i in range(30) if i % 3 == 0]
squares

#Change value to key and vice versa
capitals = {'United States': 'Washington, DC','France': 'Paris','Italy': 'Rome'}
capitals_bycapital = {capitals[key]: key for key in capitals}
capitals_bycapital        

#Sum of squares of all number from 0 to 9.
sum([i**2 for i in range(10)])

#Break a string into list
lst = [num for num in 'word']
lst

#Convert temperature in fehrenheit from celsius
celcius = [0, 10, 20.1, 34.5, 50]
fahrenheit = [(float(9/5)*temp + 32) for temp in celcius]
fahrenheit