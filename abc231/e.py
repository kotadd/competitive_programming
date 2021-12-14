# E - Minimal payments
# https://atcoder.jp/contests/abc231/tasks/abc231_e
# lru_cache と dfs
from functools import lru_cache


@lru_cache(maxsize=10000000)
def dfs(x, i):
    if x == 0:
        return 0

    r = x // A[i]
    ans = r + dfs(x % A[i], i - 1)
    if i != 0:
        ans2 = r + 1 + dfs((r + 1) * A[i] - x, i - 1)
        return min(ans, ans2)
    else:
        return ans


N, X = map(int, input().split())
A = list(map(int, input().split()))

print(dfs(X, N - 1))
