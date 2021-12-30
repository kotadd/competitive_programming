#  D - Journey
# https://atcoder.jp/contests/abc194/tasks/abc194_d
# 期待値
# 確率 p(p!=0) で成功する試行を、成功するまで行うときの試行回数(最後の成功した回も含む) の期待値は 1/pである。
# 「有効なのが来るまでカードを引く期待値は、有効なカードを引く確率の逆数になる。」


N = int(input())

ans = 0
for i in range(1, N):
    ans += N / (N - i)
print(ans)
