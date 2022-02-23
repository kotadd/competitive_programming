N = int(input())
A = [list(map(int, input().split())) for _ in range(N * 2 - 1)]

used = [False] * (2 * N)
ans = 0


def dfs(i, x):
    if i == N:
        global ans
        ans = max(ans, x)
        return

    for j in range(2 * N):
        if not used[j]:
            used[j] = True
            break

    for k in range(j + 1, 2 * N):
        if not used[k]:
            used[k] = True
            dfs(i + 1, x ^ A[j][k - j - 1])
            used[k] = False
    used[j] = False


dfs(0, 0)
print(ans)
