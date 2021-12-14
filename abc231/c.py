from bisect import bisect_left

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(Q):
    x = int(input())
    r = bisect_left(A, x)
    print(N - r)
