# B - Nice Grid
# https://atcoder.jp/contests/abc264/editorial/4578
# チェビシェフ距離（チェス盤距離）

R, C = map(int, input().split())

if max(abs(R - 8), abs(C - 8)) % 2 == 0:
    print('white')
else:
    print('black')
