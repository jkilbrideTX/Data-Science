##   Create a program, gpacalc.py, that takes four letter grade arguments and prints
##      out the corresponding GPA, to two decimals. Your program should work both in
##      arguments are upper-case and lower-case.

##Your program should print in the form:
##   “My GPA is x”
##   Where x = GPA calculation


import sys

gpa_dict = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0,'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}

def gpacalc():

    ## assign inputs to variables
    grade1 = sys.argv[1].upper()
    grade2 = sys.argv[2].upper()
    grade3 = sys.argv[3].upper()
    grade4 = sys.argv[4].upper()
    
## Perform the calculations and find average
    x = (gpa_dict [grade1] + gpa_dict [grade2] + gpa_dict [grade3] + gpa_dict [grade4]) / 4
#    x = round(gpa_total,2)

## print results
#  convert to 1.00 using an f-string function
#  https://www.codeease.net/programming/python/python-convert-1-to-1-00
    print("My GPA is"f"{x: .2f}")

gpacalc()
