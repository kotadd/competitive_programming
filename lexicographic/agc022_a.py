# A - Diverse Word
# https://atcoder.jp/contests/agc022/tasks/agc022_a

from collections import defaultdict
import string


d = defaultdict(int)
S = input()

for s in S:
    d[s] += 1

for s in string.ascii_lowercase:
    if d[s] == 0:
        print(S + s)
        exit()

for k in reversed(range(len(S))):
    s = S[k]
    for i in range(len(string.ascii_lowercase)):
        if s == string.ascii_lowercase[i]:
            for j in range(i + 1, len(string.ascii_lowercase)):
                if d[string.ascii_lowercase[j]] == 0:
                    print(S[0:k] + string.ascii_lowercase[j])
                    exit()
            break
    d[s] = 0

print(-1)
