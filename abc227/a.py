N, K, A = map(int, input().split())
ans = (K + A - 1) % N
if ans == 0:
    print(N)
else:
    print(ans)
