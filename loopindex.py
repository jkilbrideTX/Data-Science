#  Create a program, loopindex.py. Your program should:
#  Convert these string-type integers into integer-type.
#  For each of the numbers in the list, add its own index position.
#  Example 1 - If the argument is ['5', '5', '5'],
#  the program should print:[5, 6, 7]


import sys


def loop():

    ##  input of sys string
    loop_list = sys.argv[1:]
    
    ##  convert to integers
    loop_list = list(map(int, loop_list))

    ## create an empty new list
    list_new = []

    ##  loop through the list and use enumerate as a counter for i
    for i, number in enumerate(loop_list): # index p. 104

        ##  new list is the integers plus add itiona of their placement based on i
        list_new .append(number + i)
    print(list_new )

loop()
