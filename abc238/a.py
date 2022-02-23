from math import log2
n = int(input())

if 2 * log2(n) / n < 1:
    print('Yes')
else:
    print('No')
