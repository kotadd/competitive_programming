n = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if L[i] == L[j] or L[j] == L[k]:
                continue
            # 三角形のできる条件：短い辺の合計が長い辺より長くなること
            if L[i] + L[j] <= L[k]:
                continue
            ans += 1

print(ans)
