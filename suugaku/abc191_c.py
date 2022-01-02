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


# dxy = [(1, 0), (0, 1), (0, 0), (1, 1)]
# S = [list(input()) for _ in range(H)]
# ans = 0
# for i in range(H - 1):
#     for j in range(W - 1):
#         tmp = 0
#         for p in dxy:
#             dx = i + p[0]
#             dy = j + p[1]
#             if S[dx][dy] == '#':
#                 tmp += 1
#         if tmp % 2 == 1:
#             ans += 1

# print(ans)
