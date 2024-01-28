##   Create a program, duplicates.py. It should:
##    a. Remove all duplicate words from the list
##    b. Then print it in descending order of alphabets (from Z to A)

##  duplicated_words = sys.argv[1:]

##  The above duplicated_words is a list-type variable which \
##   contains a whole bunch of lower-cased words \
##   (ex. ['hello', 'world', 'welcome', 'hello', 'again']).

##  Example 1 - If the list is ['hello', 'world', 'welcome', 'hello', 'again'], 
##   the program##  should print:['world', 'welcome', 'hello', 'again']

##  Example 2 - If the list is ['apple', 'banana', 'apple', 'orange', 'pear', 'banana'],
##    the program should print:['pear', 'orange', 'banana', 'apple']


import sys

def dups():
  duplicated_words = sys.argv[1:]
  
  x = duplicated_words
  
  # sort out the duplicates
  y = (sorted(set(x), key = x.index))

  # sort the remaining list in descending order
  print(sorted(y, reverse = True))

dups()
