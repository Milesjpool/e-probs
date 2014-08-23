__author__ = 'Miles'

import math

def triangle_num(required):
    i = required
    divisors = 0
    while divisors <= required:
        divisors = 2
        num = get_tri_num(i)
        for j in range(2, int(math.sqrt(num) + 0.5)):
            if num%j == 0:
                divisors += 2
        else:
            i += 1
    return num



def get_tri_num(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


print(triangle_num(500))