# https://atcoder.jp/contests/abc226/submissions/27082752
# C - Martial artist
# N 頂点からなるグラフ
import collections

N = int(input())
# setでグラフを作る
G = [set() for _ in range(N)]
T = [0] * N
A = [[] for _ in range(N)]

for i in range(N):
    X = list(map(int, input().split()))
    T[i] = X[0]
    K = X[1]
    if K > 0:
        for x in X[2:]:
            # requiredを詰める
            G[i].add(x - 1)


# やらなければいけない武術のリスト
s = set([N - 1])
# N-1の武術からrequiredを辿っていくための用意
q = collections.deque([N - 1])

while q:
    x = q.popleft()
    for y in G[x]:
        if y not in s:
            s.add(y)
            q.append(y)

ans = 0
for x in s:
    ans += T[x]
print(ans)
