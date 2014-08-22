__author__ = 'Miles'


def fibonacci(max):
    total = 0
    a = 1
    b = 1
    while b < max:
        if b%2 == 0:
            total += b
        temp = b
        b += a
        a = temp
    return total

print(fibonacci(4000000))