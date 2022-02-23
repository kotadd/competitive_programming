from collections import deque
N = int(input())
S = input()


que = deque([N])
for i in reversed(range(N)):
    if S[i] == 'R':
        que.appendleft(i)
    else:
        que.append(i)

print(*que)
