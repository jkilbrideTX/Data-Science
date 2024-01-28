##   Create a program, counter.py. 
##   You are given a single string argument. Print a
##   dictionary where the keys are composed of each letter from a word and values
##   are the sum of each letters’ appearances. The key order should be in the order of
##   the letters’ appearances.
##      Example 1 - If the word is “good”, the program should print:
##               {'g': 1, 'o': 2, 'd': 1}
##      Example 2 - If the word is “onomatopoeia”, the program should print:
##           {'o': 4, 'n': 1, 'm': 1, 'a': 2, 't': 1, 'p': 1, 'e': 1, 'i': 1}

import sys

def count():
  text = sys.argv[1]
  letter_counter = {}
  ##  loop through the word
  for x in text:
    if x not in letter_counter:
      letter_counter[x] = 0  #if letter not in current counter, then 0
    letter_counter[x] += 1  # if letter in counter already, add 1 each additional time
  print(letter_counter)

count()



