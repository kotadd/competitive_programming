# D - Gathering Children
# https://atcoder.jp/contests/abc136/tasks/abc136_d
# Lowest Common Ancestor, LCA, 最近共通祖先 がbetter

S = input()
N = len(S)

L = [0] * N

a = 0
b = 0
for i in range(N):
    if S[i] == 'R':
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    else:
        if a == 0 and b == 0:
            continue
        if i % 2 == 0:
            L[i] += a + 1
            L[i - 1] += b
        else:
            L[i] += b + 1
            L[i - 1] += a
        a = 0
        b = 0

S = S[::-1]
for i in range(N):
    if S[i] == 'L':
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    else:
        if a == 0 and b == 0:
            continue
        if i % 2 == 0:
            L[-i - 1] += a + 1
            L[- i] += b
        else:
            L[-i - 1] += b + 1
            L[- i] += a
        a = 0
        b = 0

ans = []
for l in L:
    if l > 0:
        ans.append(l - 1)
    else:
        ans.append(l)

print(*ans)


# log2(10 ** 5) ≒ 16.6 → 最終的にans[17][]が求まれば良い。
LOG = 18


# https://qiita.com/Kept1994/items/ea91c057b0e552323da3
# lca利用

# def main():
#     S = input()
#     N = len(S)
#     to = []
#     for _ in range(LOG):
#         l = [0] * N
#         to.append(l)

#     for i in range(N):
#         to[0][i] = i + 1 if S[i] == "R" else i - 1

#     for i in range(1, LOG):
#         for j in range(N):
#             to[i][j] = to[i - 1][to[i - 1][j]]

#     ans = [0] * N
#     for j in range(N):
#         ans[to[LOG - 1][j]] += 1

#     L = [str(i) for i in ans]
#     print(" ".join(L))
#     return
