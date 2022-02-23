# D - Preparing Boxes
# https://atcoder.jp/contests/abc134/tasks/abc134_d
N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
for i in reversed(range(N)):
    tmp = A[i]
    for j in range(i + 1, N + 1, i + 1):
        tmp ^= ans[j - 1]
    ans[i] = tmp

print(sum(ans))
print(*[i + 1 for i in range(N) if ans[i]])
