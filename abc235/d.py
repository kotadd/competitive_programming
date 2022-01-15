from collections import deque

M = 10**6
a, N = map(int, input().split())


def shift_num(x: int):
    str_x = str(x)
    return int(str_x[-1] + str_x[0:-1])


def bfs():
    dist = [-1] * M
    q = deque()

    dist[1] = 0
    q.append(1)

    while q:
        v = q.popleft()
        x = v * a

        if x < M and dist[x] == -1:
            dist[x] = dist[v] + 1
            q.append(x)

        if v > 10 and v % 10 != 0:
            y = shift_num(v)
            if y < M and dist[y] == -1:
                dist[y] = dist[v] + 1
                q.append(y)

    return dist


dist = bfs()
print(dist[N])
