# C - Guess The Number
# https://atcoder.jp/contests/abc157/tasks/abc157_c
# 桁数が少ない→全探索
# 一番大きな桁が0だとダメ→ intで下から順番に調べて、stringに変換すれば、存在しない数字を無視できる

N, M = map(int, input().split())

S = []
C = []
d = dict()
for i in range(M):
    s, c = input().split()
    s = int(s)
    if s not in d:
        d[s] = c
    else:
        if d[s] != c:
            print(-1)
            exit()

for i in range(10**N):
    s = str(i)
    if len(s) != N:
        continue
    for j in range(1, N + 1):
        if j in d and d[j] != s[j - 1]:
            break
    else:
        print(s)
        exit()
print(-1)
