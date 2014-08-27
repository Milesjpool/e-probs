__author__ = 'Miles'

import math

def even_divide(max_divisor):
    small_mult = 1
    for i in range(2, max_divisor + 1):
        i_primes = get_primes(i)
        temp = small_mult
        for j in range(i):
            if temp % i_primes[j] == 0:
                temp /= i_primes[j]
            else:
                small_mult *= i_primes[j]
    return small_mult

def get_primes(number):
    i_primes = [1] * number
    j = 2
    while not number == 1:
        while not is_prime(j):
            j += 1
        if number % j == 0:
            number /= j
            k = 0
            while not i_primes[k] == 1:
                k += 1
            i_primes[k] = j
            j = 2
        else:
            j += 1
    return i_primes


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for n in [2]+list(range(3, math.ceil(math.sqrt(number)) + 1, 2)):
        if number % n == 0:
            return False
    return True


print(even_divide(20))