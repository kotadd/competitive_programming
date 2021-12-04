# C - Many Segments
# max(l[i], l[j]) <= min(r[i], r[j])で判定したが、
# r[i] < l[j] or r[j] < l[j]で判定しても良い
N = int(input())
l = [0] * N
r = [0] * N
for i in range(N):
    t, l[i], r[i] = map(int, input().split())
    l[i] *= 2
    r[i] *= 2
    if t == 2:
        r[i] -= 1
    if t == 3:
        l[i] += 1
    if t == 4:
        l[i] += 1
        r[i] -= 1

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += (max(l[i], l[j]) <= min(r[i], r[j]))

print(ans)
