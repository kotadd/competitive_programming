# https://atcoder.jp/contests/abc227/tasks/abc227_c
# A≤B≤C かつ ABC≤N であるような正の整数の組 (A,B,C) の個数を求めてください。
N = int(input())

ans = 0

for a in range(1, N + 1):
    if a * a * a > N:
        break
    for b in range(a, N + 1):
        if a * b * b > N:
            break
        ans += N // a // b - b + 1
print(ans)


# 自分の回答
# N = int(input())
# a = 1
# b = 1
# c = N
# ans = 0
# while a <= b <= c:
#     ans += (c - b + 1)
#     b += 1
#     c = (N // (a * b))
#     if b > c or a > b:
#         a += 1
#         b = a
#         c = (N // (a * b))

#     if b > c:
#         break

# print(ans)
