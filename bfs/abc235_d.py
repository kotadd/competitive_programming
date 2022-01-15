# D - Multiply and Rotate
# https://atcoder.jp/contests/abc235/tasks/abc235_d
# ■ 問題
# 下記いずれかの操作
# 1. x を消して、 x×a=123×2=246 を新たに書きこむ。
# 2. x を文字列とみなして、123 の末尾の数字である 3 を先頭に移動させる。黒板に書かれている数は 123 から 312 に変化する。
# はじめ、黒板には 1 が書かれています。書かれている数を N に変化させるには最小で何回の操作が必要ですか？
# ただし、どのように操作しても書かれている数を N に変化させられない場合は −1 を出力してください。


from collections import deque

M = 10**6
a, N = map(int, input().split())


def shift_num(x: int):
    str_x = str(x)
    return int(str_x[-1] + str_x[:-1])


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
