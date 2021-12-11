# D - Water Heater
# https://atcoder.jp/contests/abc183/tasks/abc183_d
# いもす法：https://imoz.jp/algorithms/imos_method.html

N, W = map(int, input().split())

dp = [0] * (2 * 10**5 + 1)
for i in range(N):
    s, t, p = map(int, input().split())
    dp[s] += p
    dp[t] -= p

for i in range(2 * 10**5):
    dp[i + 1] += dp[i]
    if dp[i + 1] > W:
        print('No')
        exit()

print('Yes')
