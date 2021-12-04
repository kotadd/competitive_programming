#  D - Play Train
# https://atcoder.jp/contests/abc225/tasks/abc225_d
from collections import defaultdict, deque
N, Q = map(int, input().split())

next_dict = defaultdict(int)
before_dict = defaultdict(int)
for i in range(Q):
    X = list(map(int, input().split()))

    if X[0] == 1:
        next_dict[X[1]] = X[2]
        before_dict[X[2]] = X[1]
    elif X[0] == 2:
        next_dict[X[1]] = 0
        before_dict[X[2]] = 0
    else:
        next_q = deque([X[1]])
        before_q = deque([X[1]])
        ans_a = [X[1]]
        ans_b = []
        while next_q:
            a = next_q.popleft()
            if next_dict[a] > 0:
                ans_a.append(next_dict[a])
                next_q.append(next_dict[a])
        while before_q:
            b = before_q.popleft()
            if before_dict[b] > 0:
                ans_b.append(before_dict[b])
                before_q.append(before_dict[b])

        ans = ans_b[::-1] + ans_a
        print(len(ans), *ans)
