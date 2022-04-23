# C - Connect 6
# https://atcoder.jp/contests/abc241/tasks/abc241_c
# 6つ連続できるか
# X個の連続チェックをする場合は、累積和の利用がいる

N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        tmp4 = 0
        for k in range(6):
            if i + 5 < N:
                if S[i + k][j] == '#':
                    tmp1 += 1
            if j + 5 < N:
                if S[i][j + k] == '#':
                    tmp2 += 1
            if i + 5 < N and j + 5 < N:
                if S[i + k][j + k] == '#':
                    tmp3 += 1
            if i + 5 < N and j - 5 >= 0:
                if S[i + k][j - k] == '#':
                    tmp4 += 1

            if tmp1 == 4 or tmp2 == 4 or tmp3 == 4 or tmp4 == 4:
                print('Yes')
                exit()

print('No')
