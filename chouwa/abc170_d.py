# D - Not Divisible
# https://atcoder.jp/contests/abc170/tasks/abc170_d
# i!=jの任意の整数j(1<=j<=N)について、AiはAjで割り切れない

# 調和級数的計算量
# エラトステネスの篩 (O(NlogN)) の考え方を使う。
# 下記のような計算をO(NlogN)で計算できる
# for i in range(N):
# for j in range(i,N,i)

from collections import Counter
N = int(input())
A = sorted(list(map(int, input().split())))
c = Counter(A)

max_a = A[-1]
dp = [True] * (max_a + 1)
dp[0] = False

ans = 0
for i in range(N):
    x = A[i]
    # すでにfalseになっているのであれば、それ以降もfalse
    if not dp[x]:
        continue
    # 2つ同じ数がある場合は条件を満たさない
    if c[x] == 1:
        ans += 1
    y = x
    while y <= max_a:
        dp[y] = False
        y += x
print(ans)
