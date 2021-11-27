D, G = map(int, input().split())
P = []
C = []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

ans = 1000
for i in range(1 << D):
    total = 0
    num = 0
    for j in reversed(range(D)):  # 点数が大きい順に見ないと、先に点数低いものの最大値を見てしまうため
        if i & (1 << j):
            for k in range(P[j]):
                total += 100 * (j + 1)
                num += 1
                if k == P[j] - 1:
                    total += C[j]
                if G <= total:
                    ans = min(ans, num)
                    break
print(ans)
