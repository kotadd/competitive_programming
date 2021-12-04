# C - Ringo's Favorite Numbers 2
# A-Bが200の倍数 ＝ Aを200で割った余りとBを200で割った余りが等しい
# 制約： 2 <= N <= 2×10^5
from collections import Counter
N = int(input())
A = [i % 200 for i in list(map(int, input().split()))]

C = Counter(A)

ans = 0
for c in C:
    ans += (C[c] * (C[c] - 1)) // 2
print(ans)
