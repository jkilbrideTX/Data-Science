## Create a program, diffset.py. Your program should:
##   a. Find the words that exists in set_a but are not in set_b.
##   b. Print the output in a set format.

##   Example 1 - If the set_a is ['apple', 'cherry'],
##     the program should print:{'cherry'}

import sys

set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']
diff = set(set_a).difference (set(set_b))
print (diff)
