n = int(input())

cnt = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1

if cnt.count(1) == n - 1:
    print('Yes')
else:
    print('No')
