# -*- coding: utf-8 -*-
"""
@author: Suresh Reddy Nusi
"""

"""
NumPy is a fundamental third-party package for scientific computing with Python. It contains:
A powerful N-dimensional array object.
Sophisticated (broadcasting) functions.
Useful linear algebra, Fourier transform, and random number capabilities.
Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data.
 Due to arbitrary data-types, NumPy can seamlessly and speedily integrate with a wide variety of databases.
If you are using the standalone version of Python then NumPy package to be downloaded and installed. Whereas, it is already wrapped with Anaconda package.
"""
"""
The main object in NumPy is the homogeneous multidimensional array. 
It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
 In NumPy dimensions are called axes.
"""

#All third party packages require to be imported first in Python. 'np' is used to simplify and avoid repeating 'numpy' all time. You can choose any other name.
import numpy as np

#A simple NumPy array can be defined by providing a single list of numbers as an argument.
np_list = np.array([1, 2, 3])
print("1 dimensional array = ", np_list)

#A Numpy matrix can be defined by providing sequences of sequences.
matrix_2d = np.array ([[1, 2, 3], [4, 5, 6]])
print("2 dimensional array = ", matrix_2d)

a = np.array([[1, 2, 3], [4, 5, 6]])

# the dimensions of the array.
print('shape = ', a.shape)

# the number of axes (dimensions) of the array.
print('dimension = ', a.ndim)

# an object describing the type of the elements in the array.
print('data type = ', a.dtype.name)

# the size in bytes of each element of the array.
print('size in bytes = ', a.itemsize)

# the total number of elements of the array.
print('total no. of elements = ', a.size)

print('type = ', type(a))

#Range function in Numpy
print('Range 0 to 9 with step 1 difference = ', np.arange(0, 10))

#Range function in Numpy with step difference
print('Range 0 to 10 with step 2 difference = ', np.arange(0, 11, 2))

#linspace is similar to arange, but uses a number of samples instead of step size. The endpoint can be optionally excluded.

#Range function in Numpy
print('Elements from 0 to 10 with 50 samples = ', np.linspace(0, 10, 50))

#NumPy offers several functions to create arrays if the elements of an array are originally unknown, but its size is known.
# It minimizes the necessity of growing arrays.


print('array of zeros = ', np.zeros((5, 5))) #Create array of zeros

print('array of ones = ', np.ones((2, 3, 4), dtype=np.int16)) #Create array of ones & data type can be specified

print('empty array = ', np.empty((2, 3))) #Create array with very small values

print('Identity matrix = ', np.eye(4)) #Create identity matrix
"""
Numpy.random.rand is used to create an array of the given shape and populate it with random samples from a uniform distribution between 0 and 1.

"""
print('Single integer number = ', np.random.randint(24, 110))

print('Multiple integer number = ', np.random.randint(24, 110, 10))

print('Array of random numbers = ', np.random.rand(10))

print('Matrix of random numbers = ', np.random.rand(5, 5))

#Reshaping NumPy arrays can be done through ‘reshape’ method

#Define an array of shape (1, 25)
arr = np.arange(0, 25)
print('Array with dimension (1, 25) = ', arr)

#Change the dimensions from (1, 25) to (25, 1).
mod_array = arr.reshape(25, 1)
print('Array with dimension (25, 1) = ', mod_array)

#Indexing and Slicing of NumPy array are somewhat similar to List.
arr = np.arange(0, 25)
print('arr = ', arr)

#For addressing the nth element, we will use index = n-1
print('9th element of arr = ', arr[8])

#Print elements from position 1 to 6
print('elements from position 1 to 6 = ', arr[:5])

#Print elements from position 2 to 6
print('elements from position 2 to 6 = ', arr[1:5])

#Print the last element
print('the last element = ', arr[-1])

#Print all elements in reverse order
print('all elements in reverse order = ', arr[::-1])

"""
Multidimensional Array or Matrix
Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:
"""
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))

#First print the 2D array
print('2D array = ', arr_2d)

#Print the element at 2nd row and 1st column using arr_2d[row index][column index]
print('Element at 2nd row and 1st column = ', arr_2d[1][0])

"""
Slicing is a part of array so any change made to slice object shall change the array object. Check the example below:

"""

arr = np.arange(0, 25)
print('arr before slicing= ', arr)

slice_of_arr = arr[0:6]
print('slice_of_arr = ', slice_of_arr)

#Change all elements of slice_of_arr
slice_of_arr[:] = 99

print('arr after change in slicing= ', arr)

"""
In above example, the changes made to slice_of_arr was reflected original array. The solution is to copy the array instead of slice.
"""

arr = np.arange(0, 25)
print('arr before slicing= ', arr)

arr_copy = arr.copy()
print('arr_copy = ', arr_copy)

#Change all elements of arr_copy
arr_copy [:] = 99

#Print arr to check if change reflected or not
print('arr after slicing and change in arr_copy = ', arr,arr_copy)

"""
Numpy Basic Operations
Numpy arrays operate element by element. For e.g. While adding two Numpy array, element 1 will be added to element 1 and so on.

"""

#import numpy as np
arr = np.arange(0, 10)

#Add
print('arr + arr = ', arr + arr)

#Subtract
print('arr - arr = ', arr - arr)

#Multiply
print('arr x arr = ', arr * arr)

#Divide
print('arr / arr = ', arr / arr)


#Square root of arr
print('Square root of arr = ', np.sqrt(arr))

#Exponent of arr
print('\nExponent of arr = ', np.exp(arr))

#Sine of arr
print('\nSine of arr = ', np.sin(arr))

#Log of arr
print('\nLog of arr = ', np.log(arr))

#Transpose Function
#Create an array with random numbers of dimension (3, 4)
a = np.floor(10*np.random.random((3,4)))
print('a = ', a)

#We will use 'T' method for transpose.
print('Transpose of a = ', a.T)

