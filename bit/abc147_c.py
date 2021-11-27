N = int(input())

# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1],...]
A = [[-1] * N for _ in range(N)]

for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        A[i][x - 1] = y
# A = [[-1, 1, -1], [1, -1, -1], [-1, 0, -1]]

ans = 0

for i in range(1 << N):
    honests = [0] * N
    for j in range(N):
        if i & (1 << j):
            # フラグの立った人が正直者だと仮定
            honests[j] = 1
    ok = True
    for j in range(N):
        # 正直者の人jにおいて、
        if honests[j]:
            for k in range(N):
                # 何も言っていない対象はスルー
                if A[j][k] == -1:
                    continue
                # 正直者の人jの言っている内容と正直者の結果が一致しないとき、
                if A[j][k] != honests[k]:
                    ok = False
    if ok:
        ans = max(ans, honests.count(1))

print(ans)
