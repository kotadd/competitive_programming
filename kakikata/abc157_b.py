# B - Bingo
# https://atcoder.jp/contests/abc157/tasks/abc157_b
# ビンゴのチェック

A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))
answers = [[0] * 3 for _ in range(3)]
N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                answers[i][j] = 1


# ビンゴカード（3×3 のチェック）
def is_bingo(X):
    if X[0][0] == 1 and X[0][1] == 1 and X[0][2] == 1:
        return True
    elif X[1][0] == 1 and X[1][1] == 1 and X[1][2] == 1:
        return True
    elif X[2][0] == 1 and X[2][1] == 1 and X[2][2] == 1:
        return True
    elif X[0][0] == 1 and X[1][0] == 1 and X[2][0] == 1:
        return True
    elif X[0][1] == 1 and X[1][1] == 1 and X[2][1] == 1:
        return True
    elif X[0][2] == 1 and X[1][2] == 1 and X[2][2] == 1:
        return True
    elif X[0][0] == 1 and X[1][1] == 1 and X[2][2] == 1:
        return True
    elif X[2][0] == 1 and X[1][1] == 1 and X[0][2] == 1:
        return True
    else:
        return False


print('Yes' if is_bingo(answers) else 'No')
