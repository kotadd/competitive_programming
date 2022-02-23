# E - Coprime
# https://atcoder.jp/contests/abc177/tasks/abc177_e
# エラトステネスのふるい
# gcdの問題だが、条件を考えるとgcdは利用しなくても良い

N = int(input())
A = list(map(int, input().split()))

# max(A)を計算するよりも、最大値の方が速い
M = 10**6
cnt = [0] * (M + 1)

for a in A:
    cnt[a] += 1

is_pairwise_coprime = True
for i in range(2, M + 1):
    total = 0
    for j in range(i, M + 1, i):
        total += cnt[j]

    if total == N:
        print('not coprime')
        exit()

    if total >= 2:
        is_pairwise_coprime = False
else:
    if is_pairwise_coprime:
        print('pairwise coprime')
    else:
        print('setwise coprime')
