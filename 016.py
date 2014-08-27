__author__ = 'Miles'


def pow_sum(index):
    power = str(2**index)
    total = 0
    for i in range(len(power)):
        total += int(power[i])
    return total

print(pow_sum(1000))

#Or in 1 line
#print(sum([int(i) for i in str(2**1000)]))