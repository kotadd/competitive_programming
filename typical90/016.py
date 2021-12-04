# 工夫した全探索
import sys
input = sys.stdin.readline

N = int(input())
A, B, C = map(int, input().split())

L = 10000
ans = L


for i in range(L):
    a = i * A
    for j in range(L - i):
        b = j * B
        if a + b > N or (N - a - b) % C != 0:
            continue
        k = (N - a - b) // C
        if ans > i + j + k:
            ans = i + j + k

print(ans)
