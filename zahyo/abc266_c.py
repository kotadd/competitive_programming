# C - Convex Quadrilateral
# https://atcoder.jp/contests/abc266/editorial/4659
# https://atcoder.jp/contests/abc266/submissions/34372724
# 外積

xy = []
for i in range(4):
    xy.append(list(map(int, input().split())))

for i in range(4):
    x1, y1 = xy[i]
    x2, y2 = xy[(i + 1) % 4]
    x3, y3 = xy[(i + 2) % 4]
    dx1, dy1 = x1 - x2, y1 - y2
    dx2, dy2 = x3 - x2, y3 - y2
    if dx1 * dy2 - dx2 * dy1 > 0:
        print('No')
        exit()

print('Yes')
