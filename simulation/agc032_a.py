# A - Limited Insertion
# https://atcoder.jp/contests/agc032/tasks/agc032_a
# 操作を逆順に捉え、Bの最も右側の要素を取り出すことを考える

N = int(input())
B = list(map(int, input().split()))

ans = []
i = 0
while len(ans) < N:
    if B[0] != 1:
        print(-1)
        exit()
    cur = 0
    for j in range(N - len(ans)):
        if B[j] == j + 1:
            cur = j
    ans.append(B.pop(cur))
for a in reversed(ans):
    print(a)
