__author__ = 'Miles'

import math

def route_perms(grid):
    return math.factorial(grid*2)/(math.factorial(grid)*math.factorial(grid))


print(route_perms(20))