import sys

x = int(sys.argv[1])

def in_range():
    number = []
    for i in range(3000, 5000):
        if (i % x == 0) and i % (x+7) == 0 and i % (x**2) == 0 :
            number.append(i)
    print(number)

in_range()
