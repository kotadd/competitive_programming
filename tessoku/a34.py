# A34 - Game 3
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ah
# Grundy数
# Game1(A32)とGame2(A33)の解法を組み合わせると、Game3(A34)の解法が得られる。

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

len = max(A)
dp = [-1] * (len + 1)
dp[0] = 0

for i in range(len + 1):
    if i >= X and i >= Y and (dp[i - X] == 0 or dp[i - Y] == 0):
        # 「X個もY個も取れる」かつ「X個かY個を取った後に負けの状態に遷移できる」場合は必勝
        tmp = [0, 0, 0]
        tmp[dp[i - X]] = 1
        tmp[dp[i - Y]] = 1
        for j in range(3):
            if tmp[j] == 0:
                dp[i] = j
                break
    elif i >= X and dp[i - X] == 0:
        # 「X個取れる」かつ「X個取った後に負けの状態に遷移できる」場合は必勝
        dp[i] = 1
    elif i >= Y and dp[i - Y] == 0:
        # 「Y個取れる」かつ「Y個取った後に負けの状態に遷移できる」場合は必勝
        dp[i] = 1
    else:
        # 「X個もY個も取れない」もしくは「負けの状態に遷移できない」場合は必敗
        dp[i] = 0

XOR_SUM = 0
for a in A:
    XOR_SUM ^= dp[a]

print('First' if XOR_SUM else 'Second')
