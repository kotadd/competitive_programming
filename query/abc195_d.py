# D - Shipping Center
# https://atcoder.jp/contests/abc195/tasks/abc195_d
# 荷物の大きさWi, 価値Viなど書いているのでdpのように見えるが、実際は普通にクエリを処理するだけで良い
N, M, Q = map(int, input().split())
A = []
for i in range(N):
    w, v = map(int, input().split())
    A.append([v, w])

A.sort(reverse=True)

X = list(map(int, input().split()))

for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    x = []
    for j in range(M):
        if j < l or r < j:
            x.append(X[j])
    x.sort()
    used = [False] * len(x)
    ans = 0
    for j in range(N):
        for k in range(len(x)):
            if A[j][1] <= x[k] and not used[k]:
                ans += A[j][0]
                used[k] = True
                break

    print(ans)
