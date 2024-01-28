## Create a program, comprehension.py. Your program should:
#   1. Convert these string-type integers into integer-type.
##  2. If the number within the list is divisible by 3, multiply it by 10, then replace
##    it.
##  my_ints a list-type variable which contain numbers that are
##    string-typed (ex. ['1', '2', '3', '4', '5'])


import sys

my_ints = sys.argv[1:]
# my_ints = ['1', '2', '3', '4', '5']

def comp():
  num = [int(x) for x in my_ints]
  comp = [x * 10 if x % 3 == 0 else x for x in num]
  print(comp)

comp()

# code grade input '1' '2' '3' '4' '5'
