d = dict()
for a in range(1, 150):
    for b in range(1, 150):
        x = 4 * a * b + 3 * a + 3 * b
        if x <= 1000:
            d[x] = True

N = int(input())
S = sorted(list(map(int, input().split())))

ans = 0

for i in range(N):
    if S[i] not in d:
        ans += 1

print(ans)
