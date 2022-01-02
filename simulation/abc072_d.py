# D - Derangement
# https://atcoder.jp/contests/abc072/tasks/arc082_b

N = int(input())
P = list(map(int, input().split()))

dups = 0
doubles = 0

flg = True
for i in range(N):
    if P[i] == i + 1:
        dups += 1
        if i > 0 and P[i - 1] == i:
            if flg:
                doubles += 1
                flg = False
            else:
                flg = True
        else:
            flg = True

print(doubles + (dups - (doubles * 2)))
