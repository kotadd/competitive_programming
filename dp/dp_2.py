# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# ナップサック問題

N, W = map(int, input().split())

weights = []
values = []

# dpテーブル作成
# column側が重み、raw側がindex
dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]


for i in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

for i in range(N):
    for w in range(W + 1):
        if w >= weights[i]:
            dp[i + 1][w] = max(dp[i][w], dp[i][w - weights[i]] + values[i])
        # weights[i]がwより重い時は選択できない
        else:
            dp[i + 1][w] = dp[i][w]

print(dp[N][W])
