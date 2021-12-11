# https://atcoder.jp/contests/abc166/tasks/abc166_d
#  D - I hate Factorization
X = int(input())

for i in range(-120, 120):
    x = i**5
    for j in range(-120, 120):
        y = j**5
        if x - y == X:
            print(i, j)
            exit()
