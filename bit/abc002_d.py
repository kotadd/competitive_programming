# python3でないとMLE(メモリ制限オーバー)になった
# pypyはJITを利用しているので、高速化のためにメモリを使いすぎることがあることを認識。
from itertools import combinations

N, M = map(int, input().split())

R = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    R[x - 1][y - 1] = R[y - 1][x - 1] = 1

ans = 1
for i in range(1 << N):
    S = []
    for j in range(N):
        if i & (1 << j):
            S.append(j)

    for i in list(combinations(S, 2)):
        if R[i[0]][i[1]] == 0:
            break
    else:
        ans = max(ans, len(S))

print(ans)
