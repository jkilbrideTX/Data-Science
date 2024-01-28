##  Month Abbreviations
##
##   Month abbreviations program
##    Input month abbreviation requested
##    Output: 3-letter abbreviated month

def main():
    num = int(input("What number abbreviation do you want?" ))
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',\
              'SEP', 'OCT', 'NOV', 'DEC']
    ## use -1 due to the months indexed starting at 0
    ## number asked will not account for 0 position
    print(months[num-1])

main()
