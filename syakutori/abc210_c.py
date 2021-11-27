# https://atcoder.jp/contests/abc210/submissions/me
from collections import defaultdict
# 尺取り法

N, K = map(int, input().split())
C = list(map(int, input().split()))
# 初期値を0にしてくれる便利なやつ
d = defaultdict(int)
ans = 0
cnt = 0

for i in range(K):
    d[C[i]] += 1
    if d[C[i]] == 1:
        cnt += 1
    ans = max(ans, cnt)

for i in range(K, N):
    d[C[i - K]] -= 1
    if d[C[i - K]] == 0:
        cnt -= 1

    d[C[i]] += 1
    if d[C[i]] == 1:
        cnt += 1

    ans = max(ans, cnt)

print(ans)
