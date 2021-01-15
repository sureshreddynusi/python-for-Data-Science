# -*- coding: utf-8 -*-
"""
@author: suresh reddy nusi
"""

"""
Following comparison operator are used to compare two values. The output is 'True' or 'False'.

, == Equal
, != Not Equal
, > Greater than
, < Less than
, >= Greater than equal to
, <= Less than equal to
"""

2==2

1==2

2!=1

10>=5

"""
Range is a function that return all integer numbers between two arguments
 say a, b (including a but excluding b) with given step difference.

Range (a, b, step_difference)
"""

x = list(range(0,10))
print(x)
x = list(range(0,10,2))
print(x)

"""
List and Dictionary (dict) are Data Containers in Python 
which can be used to effectually store long list of information.
The decision to use list or dict depends on use case.
"""
"""
Definition: List is defined using Square brackets [ ]
Example: month = [‘Jan’, ‘Feb’, ’Mar’]
Element Reference: Each element in the list is referred with its position starting from zero.
month [1] = ‘Feb’
"""
my_list = [1, 2, 3, 'string', '1.0']
#Each element in a List is referred to its position (always start from '0')
my_list[0]
#Index method to be used to get the position of element
my_list.index('string')
#Return how many elements are avaialble in our list (so elements can be referred from '0' to '4')
len(my_list)
#Assigning Values to List.
#The position of each element is used to assign values.
my_list[2] = 4
my_list
#Adding new elements to List
#append method always add item at the end of List.
my_list.append('new item')
my_list
# or use + operator to add new elements
my_list + ['another item']
my_list
#or use insert method to add element at particular position
my_list.insert(0, 1)
my_list

#Deleting an element from a List can be done using pop method with its position.
my_list.pop(0)
my_list

#use remove method to delete a particular element in a list (this method will remove all duplicate values so be careful)
my_list.remove('string')
my_list

#Addition of two list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_3 = list_1 + list_2
list_3

#Slicing
#Return all values before the third element
list_3[:3]

#Return all values after the third element including the third one
list_3[3:]

#Return all values between the 2nd and 4th element including 2nd and excluding 4th
list_3[2:4]

#Return every 2nd value starting from 0th element
list_3[0::2]

#Return last element
list_3[-1]

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
#matrix formation using list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]
#Element reference in a matrix
matrix[0]

matrix[0][2]


"""
Definition: Dict is defined using curly brackets { }
Example: capitals = {'Italy':'Rome', 'Germany':'Berlin', 'Malaysia':'Kualalumpur'} Element reference: Each element is referred with its key. Value can be duplicated whereas key is unique. capitals['Italy'] = 'Rome'
"""
#Simple Dictionary structure where each 'value' can be referred with its unique 'key'.
my_dict = {'key1':'value1', 'key2':'value2', 'key3': 'value3'}
my_dict['key2']
#Example
capitals = {'Rome':'Italy', 'Germany':'Berlin', 'Malaysia':'Kualalumpur'}
capitals
#Refer a particular value with its key
capitals['Rome']

#Adding data in dictionary
morecapitals = {'India': 'New Delhi','United Kingdom': 'London', 'United States': 'Washington DC'}
capitals.update(morecapitals)
capitals
#Delete values in dictionary
del capitals['United States']
capitals


"""
Dictionary can be nested and sub nested with multiple lists as well as dictionaries.
"""
#Nested Dictionary Structure with List
my_dict = {'key1':123, 'key2':[12, 33, 44], 'key3':['item1', 'item2', 'item3']}
my_dict['key3'][0]
#Nested Dictionary Structure with Dictionary where multiple keys are used to refer inner values.
my_dict = {'key1':123, 'key2':[12, 33, 44], 'key3':{'key4':'value1', 'key5':'value2', 'key6': 'value3'}}
my_dict['key3']['key4']
d = {'key':{'nestedkey':{'subnestedkey':'value1'}}}
d['key']['nestedkey']['subnestedkey']
#keys() function returns all first level keys
my_dict.keys()
#values() function returns all values that can be referred from first level
my_dict.values()
#Assigning Values to Dictionary.
#The unique key is used to assign values
my_dict['key1']

my_dict['key1'] = 1234

my_dict['key1'] 

#Manipulating values of Dictionary
my_dict['key1'] -= 1234
my_dict['key1']


"""
Definition: Tuple is defined using Round brackets ( )
Example: t = (1, 2, 3)
Element Reference: Each element in the tuple is referred with its position starting from zero. t [1] = ‘2’
"""
#Tuples are similiar to list except that the values are constant (can't be changed later on).
t = (1, 2, 3)
t[1]
t.index(1)


"""
Definition: Set is defined using Round brackets {}
Example: s = {1, 2, 3}
Element Reference: Each element in the set is referred with its position starting from zero. t [1] = ‘2’
"""
#Set are similiar to list except that the values are constant (can't be changed later on and also it will remove the duplicates.
s = {1, 2, 3}
s[1]
s.index(1)



"""
for loop is used to repeat a block of code for a fixed number of times or else break in between by some condition.
"""
#Repeat code 3 times.
for x in range(0, 3):
    print ("We're on time %d" % (x))
    
#Repeat code for number of letter in a string.

sentence = 'This is a string'

for letter in sentence:
    print (letter)   
    
#Repeat code for all elements in a list divisible by 2.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in list: 
    if num%2 == 0:
        print(num)    
    
#Return sum of all elements in a list_matrix = [(1, 2), (3, 5), (6, 8)]
list_sum = 0
for num in list:
    list_sum += num
print (list_sum)  


#Apply a for loop on list to get all values and their position 
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2

for index, value in enumerate(list_3):
    print("Element",index,"->",value)
    
    
#Use for loop on matrix 

#Matrix of Tuple
t_matrix = [(1, 2), (3, 5), (6, 8)]
for element in t_matrix:
    print(element)

for t1, t2 in t_matrix:
    print(t1)
    
#Matrix of List
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]

#A row can be referred using position referrence as seen above but column to be further extracted and save in aother list
first_col = [row[0] for row in matrix]
first_col


capitals = {'Rome':'Italy', 'Germany':'Berlin', 'Malaysia':'Kualalumpur'}
#Use for loop on dictionary and refer element using key
for key in capitals:
    print(key,capitals[key])
    
#Another method to return all keys and values in dictionary
for key,value in capitals.items():
    print(key,value)    
#Use for loop to get all values independant of key
for value in capitals.values():
    print(value)
    
"""
While loop is used to repeat a block of code repeatedly as long as a given condition is true.
"""
x = 0
while x<10:
    print('x is currently:', x)
    x+=1
else:
    print ('All Done')
    
    
x = 0
while x<10:
    print('x is currently:', x)
    x+=1
    if x == 3:
        print('x==3')
        break
    else:
        print ('All Done')    
        
        
"""
An if statement contains the block of code that executes when the conditional expression resolves to 1 or a TRUE value.
The elif statement is used iff you further want to test another condition on failure of first if.
The else statement is an optional statement which execute on failure of if and elif conditions.
"""

if True:
    print('it was True')
    
    
x = False

if x:
    print('x was true')
else:
    print('x was fault')    



loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to Auto Shop')
elif loc == 'Bank':
    print('Welcome to Bank')
else:
    print('Where are you?')



"""
In Python programming, especially when you're dealing with data, there are many cases where you want to iterate over list or dict, perform an operation on every element, and then collect all the results in a new list or dict. This can be done with a For Loop, but Python offers a great feature, comprehensions, that lets you write shorter and clearer code that achieves the same effect.
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