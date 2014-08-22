__author__ = 'Miles'

def fizz_buzz(number):
    sum = 0
    for x in range(0, number):
        if (x%3 == 0) or (x%5 == 0):
           sum += x
    return sum

print (fizz_buzz(1000))