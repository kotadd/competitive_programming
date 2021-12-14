# D - Pair of Balls
# https://atcoder.jp/contests/abc216/tasks/abc216_d
# M本の筒の中にボールをk個ずつ合計2N個入れ、先頭から同じ数字のものを順に取り出したときにすべてなくすことができるか？
# 筒の中のボールを A に deque のリスト形式で格納する

from collections import deque
N, M = map(int, input().split())

mem = [[] * N for _ in range(N)]
A = [deque() for _ in range(M)]

for i in range(M):
    k = int(input())
    x = list(map(int, input().split()))
    for j in range(k):
        A[i].append(x[j] - 1)

    # Aの先頭の数字が何番(i)の筒に入っているかをメモする
    mem[A[i][0]].append(i)


q = deque()
for i in range(N):
    # 先頭の数字をメモしたlistが長さ2である => 筒から取り出しても良いのでqに入れる
    if len(mem[i]) == 2:
        q.append(i)

while q:
    x = q.popleft()
    # qには筒から取り出しても良い数字のリストが入っているので、mem[x]を確認することで、どの筒(p)かわかる
    for p in mem[x]:
        # ※listのpop(0)でも先頭削除できるが、O(N)かかるため、先頭を取り出していくことが決まっている場合はdeque().popleft()を利用するべき
        A[p].popleft()
        # pの筒の先頭を取り出した後、筒にまだ残っているのであれば、その数字が先頭になるのでメモする
        if len(A[p]) >= 1:
            mem[A[p][0]].append(p)
            # メモした数字が2つになれば筒から取り出しても良いのでqに入れる
            if len(mem[A[p][0]]) == 2:
                q.append(A[p][0])

# 筒の中を確認して一つでもボールが残っていれば、No
for p in A:
    if len(p) >= 1:
        print('No')
        exit()

print('Yes')
