__author__ = 'Miles'


import math

def sum_of_primes(max):
    sum = 0
    prime = 2
    while prime < max:
        sum += prime
        prime = next_prime(prime)
    return sum


def next_prime(number):
    next = number+1
    while not is_prime(next):
        next += 1
    return next


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for n in [2]+list(range(3, math.ceil(math.sqrt(number)) + 1, 2)):
        if number % n == 0:
            return False
    return True

print(sum_of_primes(2000000))