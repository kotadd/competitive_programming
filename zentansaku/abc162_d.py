# D - RGB Triplets
# https://atcoder.jp/contests/abc162/tasks/abc162_d
from collections import Counter
N = int(input())
S = input()

c = Counter(S)

# そもそもRGB揃っていないケースを省くこと
if len(c) < 3:
    print(0)
    exit()

cnt = 0
for i in range(N):
    for j in range(1, N):
        if i + 2 * j >= N:
            break
        # RGBが異なり、等間隔の個数
        if S[i] != S[i + j] and S[i + j] != S[i +
                                              2 * j] and S[i] != S[i + 2 * j]:
            cnt += 1

ans = 1
for v in c.values():
    ans *= v

print(ans - cnt)
