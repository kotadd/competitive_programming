# D - Rectangles
# https://atcoder.jp/contests/abc218/tasks/abc218_d
# 左下の頂点と右上の頂点を決めると長方形が一意に定まることを利用

N = int(input())
p = set([tuple(map(int, input().split())) for _ in range(N)])
ans = 0
for p1 in p:
    for p2 in p:
        if not (p1[0] < p2[0] and p1[1] < p2[1]):
            continue
        q = (p1[0], p2[1])
        r = (p2[0], p1[1])

        if q in p and r in p:
            ans += 1

print(ans)
