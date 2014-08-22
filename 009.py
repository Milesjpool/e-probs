__author__ = 'Miles'

import math


def pythag_trip(sum):

    for a in range(1, sum):
        for b in range(1, sum):
            sq_sum = (a*a)+(b*b)
            c = math.sqrt(sq_sum)
            if math.sqrt(sq_sum)%1 == 0:
                if a+b+c == sum:
                    return (a*b*c)


print(pythag_trip(1000))