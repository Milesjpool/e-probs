__author__ = 'Miles'


def sum_sq_diff(max):
    sum_sq = 0
    sum = 0
    for i in range(1, max+1):
        sum += i
        sum_sq += i*i
    sq_sum = sum * sum
    diff = sq_sum - sum_sq
    return diff

print(sum_sq_diff(100))