##  SPHERE
##
##    PROGRAM:
##      Take in the radius of a sphere and get the volume and the surface area of it



def main():
    rad = float(input("What is the radius? "))
    ##  Set up the equations 
    ##  have to import math library
    from math import pi
    ## can also import math
    ##    have to use math.pi instead of just pi
    ##  assign variable for volume
    v = (4/3) * pi * (rad**3)
    ##  assign variable for area
    a = 4 * pi * (rad*2)
    
    print("The volume is:", round(v, 2), 'units cubed')
    print("The area is:", round(a, 2), 'units squared')
    
main()
