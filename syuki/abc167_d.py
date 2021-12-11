# D - Teleporter
# https://atcoder.jp/contests/abc167/tasks/abc167_d

N, K = map(int, input().split())
A = list(map(int, input().split()))

i = 0
ans = 1
d = dict()
while K > 0:
    if ans in d:
        K = K % (i - d[ans])
    else:
        d[ans] = i

    if K != 0:
        ans = A[ans - 1]
        K -= 1
        i += 1
print(ans)
