##   Create a program, commonset.py. Your program should:
##     a. Find the common words between set_a and set_b.
##     b. Print the output in a set format.

import sys

set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']
intersection = set(set_a) & set(set_b)
print(intersection)






 
