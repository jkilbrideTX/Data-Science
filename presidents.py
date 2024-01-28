##   Use the president_heights.csv file to complete the assignment. Create a
##    program, presidents.py, that takes two arguments. These arguments will
##    correspond to the start and stop of a slice, respectively. It will slice the heights
##    column in the president_heights.csv files.

##   Read in the csv data like so:

##  Then print off the average height, rounded to two decimals, of the selected 
##    presidents in the following form:

##   “The average height of presidents number x to y is z”
##  Where:
##  x = start of the slice
##  y = end of the slice
##  z = calculated average

##  Note: There would be 6 presidents if the “The average height of presidents
##   number 4 to 10 is ...” (Think in terms of index slicing when it says 4 to 10)



import sys

import pandas as pd
df = pd.read_csv("president_heights.csv")

x = int(sys.argv[1]) #slice start
y = int(sys.argv[2]) #slice stop

def pres():
  # iloc=start:stop, "height" column. mean along the rows
  pres_heights = df.iloc[x:y, 1].mean(axis = 0)

  #round to 2 decimals
  z = round(pres_heights, 2)
  print(f'The average height of presidents number {x} to {y} is {z}')

pres()
