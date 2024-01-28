##  Using the following dictionary, create a program that takes an argument (subject) and prints the average score excluding that subject, to two decimals.

#  grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

# For example:

#  If the argument is Biology, it should print 80.56
#  If the argument is Chemistry, it should print 78.5

import sys

grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

def avg_grade():
  total = 0
  key = sys.argv[1].title()
  del grades[key]
  average = round((sum(grades.values())/len(grades)), ndigits = 2)
  print(f'{average}')
    

avg_grade()
