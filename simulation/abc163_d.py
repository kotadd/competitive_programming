# D - Sum of Large Numbers
# https://atcoder.jp/contests/abc163/tasks/abc163_d

MOD = 10**9 + 7
N, K = map(int, input().split())

ans = 0

x = 0
y = N
for i in range(1, N + 2):
    total = y - x + 1
    if i >= K:
        ans += total
        ans %= MOD
    x += i
    y += N - i

print(ans)
