# C - Digital Graffiti
# https://atcoder.jp/contests/abc191/tasks/abc191_c
# 点(x,y)が頂点となる数を数える
H, W = map(int, input().split())
S = [input() for i in range(H)]
ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        ans += [S[i][j], S[i][j + 1], S[i + 1][j], S[i + 1][j + 1]].count('#') % 2
print(ans)
