# E - Fraction Floor Sum
# https://atcoder.jp/contests/abc230/tasks/abc230_e
# N/i の sum を求める
# https://kanpurin.hatenablog.com/entry/2021/12/07/211249

N = int(input())
M = int(N ** 0.5)
ans = 0
for i in range(1, M + 1):
    ans += N // i
ans = 2 * ans - M**2
print(ans)

# 別解
# N = int(input())
# ans = 0
# i = 1
# while i <= N:
#     x = N // i
#     ni = N // x + 1
#     ans += x * (ni - i)
#     i = ni
# print(ans)
