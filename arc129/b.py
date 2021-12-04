INF = float("inf")
N = int(input())
l_max = -INF
r_min = INF
for _ in range(N):
    l, r = map(int, input().split())
    l_max = max(l_max, l)
    r_min = min(r_min, r)
    if l_max <= r_min:
        print(0)
    else:
        print((l_max - r_min + 1) // 2)
