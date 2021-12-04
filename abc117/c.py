#  C - Streamline
# https://atcoder.jp/contests/abc117/tasks/abc117_c
# 移動距離の最小（区間の距離 A[i-1]~A[i] のlistを作る）

N, M = map(int, input().split())
X = sorted(map(int, input().split()))

if N >= M:
    print(0)
else:
    B = []
    ans = 0
    for i in range(1, M):
        B.append(X[i] - X[i - 1])
        ans += X[i] - X[i - 1]

    B.sort(reverse=True)

    for i in range(N - 1):
        ans -= B[i]
    print(ans)
