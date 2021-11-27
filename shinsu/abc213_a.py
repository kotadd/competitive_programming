# https://atcoder.jp/contests/abc213/tasks/abc213_a
a, b = map(int, input().split())

# bin : 2進数への変換
# int(x,2): 2進数から10進数への変換
# ^ : xor
# print(int(bin(a ^ b), 2))

# こちらで良い（bin変換不要）
print(a ^ b)

# 解法2: 等式を満たすかで見ることも可能
# for C in range(256):
#   if (A^C)==B:
#     print(C)
#     exit()
