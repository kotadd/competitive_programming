# D - Face Produces Unhappiness
# https://atcoder.jp/contests/abc140/tasks/abc140_d
# 幸福度は2ずつ増えるが、上限があるので考慮

N, K = map(int, input().split())
S = input()

cur = S[0]
ans = 0
for i in range(1, N):
    if S[i] == cur:
        ans += 1
    else:
        cur = S[i]

ans += 2 * K

print(min(N - 1, ans))
