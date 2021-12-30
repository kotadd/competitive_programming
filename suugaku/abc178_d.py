# D - Redistribution
#  すべての項が 3 以上の整数で、その総和が S であるような数列がいくつあるか

MOD = 10**9 + 7
S = int(input())
dp = [0] * (S + 1)

dp[0] = 1
for i in range(3, S + 1):
    for j in range(0, i - 2):
        dp[i] += dp[j]
        dp[i] %= MOD

print(dp[S])
