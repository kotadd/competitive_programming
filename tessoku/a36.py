# A36 - Travel
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_aj
# 偶奇を考える
N, K = map(int, input().split())

if K % 2 == 0 and (N - 1) * 2 <= K:
    print('Yes')
else:
    print('No')
