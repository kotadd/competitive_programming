# C - Takahashi's Information
# https://atcoder.jp/contests/abc088/tasks/abc088_c
# 魔法陣的なやつ？
C = [list(map(int, input().split())) for _ in range(3)]

A = [0] * 3
B = [0] * 3

ok = True
for i in range(101):
    for j in range(101):
        if C[0][0] == i + j:
            A[0] = i
            B[0] = j

            B[1] = C[0][1] - A[0]
            B[2] = C[0][2] - A[0]

            A[1] = C[1][0] - B[0]
            A[2] = C[2][0] - B[0]

            tmp = 0
            for k in range(3):
                for l in range(3):
                    if C[k][l] == A[k] + B[l]:
                        tmp += 1

            if tmp == 9:
                print('Yes')
                exit()
print('No')
