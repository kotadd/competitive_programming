import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

rowsSum = [0] * H
columnsSum = [0] * W

for i in range(H):
    for j in range(W):
        rowsSum[i] += A[i][j]
        columnsSum[j] += A[i][j]

for i in range(H):
    for j in range(W):
        print(rowsSum[i] + columnsSum[j] - A[i][j], end=' ')
    print()
