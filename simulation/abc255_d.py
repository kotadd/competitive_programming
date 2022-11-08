# D - ±1 Operation 2
# https://atcoder.jp/contests/abc255/editorial/4109

N, Q = map(int, input().split())
A = sorted(map(int, input().split()))
R = [0] * (N + 1)
for i in range(N):
    R[i + 1] = R[i] + A[i]

for i in range(Q):
    x = int(input())
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
    # kXi
    ans = x * l
    # -sigma(Aj)
    ans -= R[r + 1]
    # +sigma(An - Aj)
    ans += R[N] - R[l]
    # -Xi(N-k)
    ans -= x * (N - l)
    print(ans)
