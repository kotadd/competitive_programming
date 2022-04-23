# D - Cylinder
# https://atcoder.jp/contests/abc247/tasks/abc247_d
# ランレングス符号化

from collections import deque

que = deque()
Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        que.append(query[1])
        que.append(query[2])
    else:
        ans = 0
        val = que.popleft()
        num = que.popleft()

        while query[1] != 0:
            if num > query[1]:
                num -= query[1]
                ans += val * query[1]
                query[1] = 0
                que.appendleft(num)
                que.appendleft(val)
            elif num == query[1]:
                ans += val * num
                query[1] = 0
            else:
                ans += val * num
                query[1] -= num
                val = que.popleft()
                num = que.popleft()
        print(ans)
