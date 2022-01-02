# D - Takahashi Unevolved
# https://atcoder.jp/contests/abc180/tasks/abc180_d

x, y, a, b = map(int, input().split())

ans = 0
while a * x < y and a * x <= x + b:
    x *= a
    ans += 1

print(ans + (y - 1 - x) // b)
