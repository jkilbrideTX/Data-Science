##   Create a program called reallyrandom.py that has a function that takes in three
##    arguments and prints one integer. Set your numpy random seed to 42.

##  The first argument should correspond to the size of a np.randint that has
##    values from 0 to 10.

##  The second is an integer that you will multiply the randint by.

##  The third argument is a value you will index the result of the multiplication by.

##  The program should not crash if the third value is larger than the first.

##  You will print the integer that was indexed as ‘Your random value is x’ where x =the result of the indexing.

import sys
import numpy as np

##create three arguments
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def reallyrandom():
    ## set random seed @ 42
    np.random.seed(42)
    
    ##  prevent from crashing if 3 > 1 
    if c < a:
      
      ## first argument should correspond to the size of a np.randint (a)
      ## second is an integer that you will multiply the randint by (b)
        array = np.random.randint(0, 10, size= a, dtype=int) * b
        
        ## index the result of the multiplication by third argument (c)
        x = array[c]
        
        print(f'Your random value is {x}')

    else:
        return

reallyrandom()
