#  C - Filling 3x3 array
# https://atcoder.jp/contests/abc256/tasks/abc256_c
# 各行列の合計値のみわかっている状態で、各マスに入る値のパターンを求める

h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a in range(1, 29):
    for b in range(1, 29):
        for d in range(1, 29):
            for e in range(1, 29):
                c = h1 - a - b
                f = h2 - d - e
                g = w1 - a - d
                h = w2 - b - e
                i = w3 - c - f
                if min(c, f, g, h, i) > 0 and g + h + i == h3:
                    ans += 1


print(ans)
