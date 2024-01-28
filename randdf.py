##  Create a program called randdf.py that has a function that takes two integer
##   arguments and prints a Pandas dataframe. The two arguments will correspond
##   to the number of rows and number of columns, respectively. The dataframe
##   should be filled with random integers from 0 to 100.

##  Set your numpy random seed to 56.

## Note: Use random from numpy. Otherwise, you might get a different result.


import sys

import numpy as np
import pandas as pd

a = int(sys.argv[1]) # rows
b = int(sys.argv[2]) # columns


def randdf():
  ## set random seed @ 56
    np.random.seed(56)
    
    ## create a panda dataframe with 2 random integers. (numpy pseudorandom p. 104)
    randdf = pd.DataFrame(np.random.randint(0, 100, size=(a, b)))
    
    print(randdf)

randdf()
