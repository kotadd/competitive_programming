# D - Dice in Line
# https://atcoder.jp/contests/abc154/tasks/abc154_d

N, K = map(int, input().split())
P = list(map(int, input().split()))

kukan = []
first = 0

for i in range(K):
    first += P[i]

kukan.append(first)

ans = first
for i in range(K, N):
    tmp = kukan[-1]
    tmp += P[i]
    tmp -= P[i - K]
    kukan.append(tmp)
    if tmp > ans:
        ans = tmp

print((ans - K) / 2 + K)
