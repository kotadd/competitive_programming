N = int(input())
A = list(map(int, input().split()))

B = []

cur = 0
for a in A:
    cur += a
    cur %= 360
    B.append(cur)

B.append(0)
B.append(360)

B.sort()

ans = 0
cur = 0
for b in B:
    ans = max(ans, b - cur)
    cur = b

print(ans)
