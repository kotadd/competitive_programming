# A33 - Game 2
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ag
# ニム数（暗記する）
# 石の山が N 個あり、山 i(1≤i≤N) には Ai個の石が積まれています。
# 好きな石の山を 1 つ選び、選んだ山から 1 個以上の石を取るゲームを2人でやる場合、どちらが勝ちますか?

N = int(input())
A = list(map(int, input().split()))

XOR_SUM = 0
for a in A:
    XOR_SUM ^= a

print('First' if XOR_SUM else 'Second')
