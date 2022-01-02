# C - X drawing
# https://atcoder.jp/contests/abc230/tasks/abc230_c
# abc184_c Super Ryumaの類題？

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
    for j in range(R, S + 1):
        if i + j == A + B or i - j == A - B:
            print('#', end='')
        else:
            print('.', end='')
    print()
