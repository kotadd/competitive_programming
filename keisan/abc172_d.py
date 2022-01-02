# D - Sum of Divisors
# https://atcoder.jp/contests/abc172/tasks/abc172_d
# X の正の約数の個数 * 正整数
N = int(input())
ans = 0
for i in range(1, N + 1):
    for j in range(1, N // i + 1):
        ans += i * j

print(ans)
