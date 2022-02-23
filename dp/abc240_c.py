# C - Jumping Takahashi
# https://atcoder.jp/contests/abc240/tasks/abc240_c

N, X = map(int, input().split())
M = 10001
dp = [0] * M
dp[0] = 1

for _ in range(N):
    a, b = map(int, input().split())
    # 最後のジャンプで到達していることを見ないといけないので、途中のものは0でリセット
    nxt = [0] * 10001
    for i in range(M):
        if i + a < M:
            nxt[i + a] |= dp[i]
        if i + b < M:
            nxt[i + b] |= dp[i]
    dp = nxt

print('Yes' if dp[X] else 'No')
