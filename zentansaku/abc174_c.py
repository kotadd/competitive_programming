# C - Repsept
# https://atcoder.jp/contests/abc174/tasks/abc174_c
# 鳩ノ巣原理 でK個まで見れば良い
# 数値は毎回 %K していかないと膨大になり計算量が増えるため、TLEになる

K = int(input())

k = 0
for i in range(1, K + 1):
    k = (k * 10 + 7) % K
    if k == 0:
        print(i)
        exit()
print(-1)
