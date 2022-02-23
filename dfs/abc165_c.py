# C - Many Requirements
# https://atcoder.jp/contests/abc165/tasks/abc165_c
# 重複単調増加の組み合わせ
# dfsで解くパターン

N, M, Q = map(int, input().split())

e = [list(map(int, input().split())) for i in range(Q)]

w = [0] * N
ans = 0


# cur: 現在値、lst: 最大値
def dfs(cur, lst):
    global ans, w
    if cur == N:
        tmp = 0
        for a, b, c, d in e:
            if w[b - 1] - w[a - 1] == c:
                tmp += d
        ans = max(ans, tmp)
        return
    for i in range(lst, M + 1):
        w[cur] = i
        dfs(cur + 1, i)


dfs(0, 1)
print(ans)
