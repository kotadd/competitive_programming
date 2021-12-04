# C - X drawing
# https://atcoder.jp/contests/abc230/tasks/abc230_c
# x-y = A-B であれば右肩上がり（単調増加）
# x+y = A+B であれば右肩下がり（単調減少）
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for x in range(P, Q + 1):
    line = []
    for y in range(R, S + 1):
        if x - y == A - B or x + y == A + B:
            line.append('#')
        else:
            line.append('.')
    print("".join(line))
