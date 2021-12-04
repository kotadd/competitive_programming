# ソートして貪欲法
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

sum = 0
for i in range(n):
    sum += abs(a[i] - b[i])

print(sum)
