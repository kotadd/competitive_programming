#  B - Many Oranges
# https://atcoder.jp/contests/abc195/tasks/abc195_b
# A<=X<=B の範囲で何個取れるか？ -> O(1)で求められるし、もしくは全探索で求めることもできる

A, B, W = map(int, input().split())

lower = 10**10
upper = 0

for i in range(1, 10**6 + 1):
    if A * i <= 1000 * W <= B * i:
        lower = min(lower, i)
        upper = max(upper, i)

if upper == 0:
    print('UNSATISFIABLE')
else:
    print(lower, upper)

# O(1)の計算
# import math

# A, B, W = map(int, input().split())
# upper = int(math.floor(1000 * W / A))
# lower = int(math.ceil(1000 * W / B))

# if lower > upper:
#     print('UNSATISFIABLE')
# else:
#     print(lower, upper)
