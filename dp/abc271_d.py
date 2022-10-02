# D - Flip and Adjust
# https://atcoder.jp/contests/abc271/tasks/abc271_d

N, S = map(int, input().split())
dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
A = [[] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    A[i] = [a, b]
    for j in range(S + 1):
        if j + a < S + 1:
            dp[i + 1][j + a] |= dp[i][j]
        if j + b < S + 1:
            dp[i + 1][j + b] |= dp[i][j]

if dp[N][S] == 1:
    print('Yes')
    ans = ''
    for i in reversed(range(N)):
        if dp[i][S - A[i][0]] == 1:
            ans = 'H' + ans
            S -= A[i][0]
        elif dp[i][S - A[i][1]] == 1:
            ans = 'T' + ans
            S -= A[i][1]

    print(ans)

else:
    print('No')
