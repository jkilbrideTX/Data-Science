##    Create a program called arrayargs.py that has a function 
##      that takes four integer arguments. Those arguments should
##      be put into an Numpy array.

##    The function will have two print statements.
##    The first will print the type of the array you create 
##      (which should be <class‘numpy.ndarray’>).

##   For this, DO NOT just do print(“<class ‘numpy.ndarray’>”)
##   The second will print the multiplication of the four items 
##     in your array.

##   Your output could look like this (it could differ in parts):
##   <class ‘numpy.ndarray’>
##   80

##   Code grade impout: 4 5 4 1; 18 17 3 5; -2 -55 10000 11 
##   Code grade output:  80;       4590;     12100000




import sys

import numpy as np

# a = int(sys.argv[1])
# b = int(sys.argv[2])
# c = int(sys.argv[3])
# d = int(sys.argv[4])

array_1 = ([4, 5, 4, 1])

def number_array():
    print(type(array_1))
print(np.prod(array_1))

#number_array()