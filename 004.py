__author__ = 'Miles'


def palindrome():
    largest = 0
    for x in range(100, 999):
        for y in range(100, 999):
            curr = x*y
            if palin_chk(curr) & (curr > largest):
                largest = curr
    return largest


def palin_chk(number):
    rev = str(number)[::-1]
    if str(number) == rev:
        return True
    else:
        return False

print(palindrome())