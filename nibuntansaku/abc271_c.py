# C - Manga
# https://atcoder.jp/contests/abc271/tasks/abc271_c

# 二分探索
# 判定問題「少なくとも X 巻までを全て読むことができるか？」
# このとき、X 巻までの本は 1 冊残し、それ以外の本は全て売るとする
# 残った本＋(売った本/2)が X 以上なら答えはYes

N = int(input())
A = set(map(int, input().split()))

l = 0
r = N + 1
while r - l > 1:
    m = (l + r) // 2
    c = len(set(range(1, m + 1)) & A)
    if c + (N - c) // 2 >= m:
        l = m
    else:
        r = m

print(l)
