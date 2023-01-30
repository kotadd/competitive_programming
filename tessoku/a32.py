# ★A32 - Game 1
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_af
# 必勝法
N, A, B = map(int, input().split())

dp = [False] * (N + 1)

for i in range(N + 1):
    if i >= A and not dp[i - A]:
        # 「A個取れる」かつ「A個取った後に負けの状態に遷移できる」場合は必勝
        dp[i] = True
    elif i >= B and not dp[i - B]:
        # 「B個取れる」かつ「B個取った後に負けの状態に遷移できる」場合は必勝
        dp[i] = True
    else:
        # 「A個もB個も取れない」もしくは「負けの状態に遷移できない」場合は必敗
        dp[i] = False

print('First' if dp[N] else 'Second')
