##  Your autotest cases will NOT work if you don’t load your sys.argv like
##   below. For this assignment, load in your sys.argv like so:

##  duck_goose = sys.argv[1:]
##  The above duck_goose a list-type variable which contains lower-cased
##   words, either 'duck' or 'goose' (ex. [ 'duck', 'duck', 'goose']).

##  Create a program, duckgoose.py which removes all the ‘goose’ within the list
##   then print the remaining list.

##  Example - If the duck_goose is ['goose', 'duck', 'duck', 'goose', 'goose'], the
##    program should print: ['duck', 'duck']


import sys


duck_goose = sys.argv[1:]


def remove_words():
  ##create a blank list
  n_list = []
  
  # search for an item in the list
  for x in duck_goose:
    
    # if the item is NOT goose
    if x != 'goose':
    
     #send to new list 
      n_list.append(x)
  
  print(n_list)

remove_words()

