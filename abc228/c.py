N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

S = []
ranking = []
for i in range(N):
    total = sum(P[i])
    S.append(total)
    ranking.append(total)
ranking.sort(reverse=True)

limit = ranking[K - 1]

for score in S:
    if limit - score <= 300:
        print('Yes')
    else:
        print('No')
