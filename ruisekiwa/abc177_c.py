# https://atcoder.jp/contests/abc177/tasks/abc177_c
# 累積和
# 1≤i<j≤N を満たす全ての組 (i,j) についての Aの和

N = int(input())
MOD = 10**9 + 7

A = list(map(int, input().split()))

S = [0] * (N + 1)
ans = 0
for i in range(N):
    S[i + 1] = S[i] + A[i]

for i in range(N):
    ans += A[i] * (S[N] - S[i + 1])
    ans %= MOD

print(ans)
