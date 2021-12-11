# D - Chat in a Circle
# https://atcoder.jp/contests/abc173/tasks/abc173_d
# Median of Mediansを利用すれば O(N) で解けるらしい
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = A[0]

offset = 1
for i in range(2, N):
    ans += A[i - offset]
    if i % 2 == 0:
        offset += 1

print(ans)
