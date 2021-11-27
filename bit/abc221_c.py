N = sorted(input(), reverse=True)

ans = 0

for i in range(1 << len(N)):
    l = ''
    r = ''
    for j in range(len(N)):
        if i & (1 << j):
            l += N[j]
        else:
            r += N[j]
    if len(l) == 0 or l[0] == '0' or len(r) == 0 or r[0] == '0':
        continue
    ans = max(int(l) * int(r), ans)

print(ans)
