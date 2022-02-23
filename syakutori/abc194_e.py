# E - Mex Min
# https://atcoder.jp/contests/abc194/tasks/abc194_e
# 区間の端の計算をするだけ。尺取り法

N, M = map(int, input().split())
A = list(map(int, input().split()))

L = 15 * 10**5

cnt = [0] * (L + 1)
for i in range(M):
    cnt[A[i]] += 1

ans = L
for i in range(L):
    if cnt[i] == 0:
        ans = i
        break

for i in range(M, N):
    cnt[A[i]] += 1
    cnt[A[i - M]] -= 1

    if cnt[A[i - M]] == 0 and ans > A[i - M]:
        ans = A[i - M]

print(ans)
