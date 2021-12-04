N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i != 0 and B[i][j] != B[i - 1][j] + 7:
            print('No')
            exit()
        if j != 0 and B[i][j] != B[i][j - 1] + 1:
            print('No')
            exit()

se = set()
for j in range(M):
    se.add((B[0][j] - 1) // 7)

if len(se) == 1:
    print('Yes')
else:
    print('No')
