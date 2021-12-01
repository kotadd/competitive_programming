from collections import deque

N, M = map(int, input().split())

G = [set() for _ in range(N)]

# どの都市が繋がっているかGraphを作成する
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].add(b - 1)


ans = 0
for i in range(N):
    # スタート地点の都市をiとする
    q = deque([i])
    s = set([i])
    while q:
        x = q.popleft()
        for y in G[x]:
            if y not in s:
                s.add(y)
                q.append(y)
    # スタート地点も含み、回った都市を加算している
    ans += len(s)

print(ans)
