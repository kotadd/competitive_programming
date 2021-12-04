import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
lb, ub = 0, 10**18
while ub - lb > 1:
    m = (lb + ub) // 2
    s = 0
    for a in A:
        s += min(m, a)
    if m * K <= s:
        lb = m
    else:
        ub = m
print(lb)
