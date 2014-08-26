__author__ = 'Miles'

def collatz_seq(limit):
    longest_seq = 0
    seq_num = 0
    for i in range(1, limit+1):
        seq_length = col_len(i)
        if seq_length > longest_seq:
            longest_seq = seq_length
            seq_num = i
    return seq_num

def col_len(i):
    seq_leng = 0
    while not i == 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3*i + 1
        seq_leng += 1
    return seq_leng


print(collatz_seq(1000000))


