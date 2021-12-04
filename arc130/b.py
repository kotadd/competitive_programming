H, W, C, Q = map(int, input().split())

ans = [0] * C
T = [] * Q
N = [] * Q
COLORS = [] * Q
for i in range(Q):
    t, n, c = map(int, input().split())
    T.append(t)
    N.append(n)
    COLORS.append(c)

h = dict()
w = dict()

h_cnt = 0
w_cnt = 0

for i in reversed(range(Q)):
    t = T[i]
    n = N[i]
    c = COLORS[i]

    if t == 1:
        if n in h:
            continue
        h[n] = 1
        h_cnt += 1
        ans[c - 1] += W - w_cnt
    else:
        if n in w:
            continue
        w[n] = 1
        w_cnt += 1
        ans[c - 1] += H - h_cnt

print(*ans)
