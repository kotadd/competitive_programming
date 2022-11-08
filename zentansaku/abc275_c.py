# C - Counting Squares
# https://atcoder.jp/contests/abc275/editorial/5141
# 二次元座標平面上の正方形のカウント
S = [list(input()) for _ in range(9)]

ans = 0
for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            for k in range(i, 9):
                for l in range(j + 1, 9):
                    if S[k][l] == '#':
                        dx, dy = k - i, l - j
                        if 0 <= i + dy < 9 and 0 <= j - dx < 9 and 0 <= k + dy < 9 and 0 <= l - dx < 9:
                            if S[i + dy][j - dx] == '#' and S[k + dy][l - dx] == '#':
                                ans += 1

print(ans)


# 別解
# import itertools
# S=[input() for _ in range(9)]
# ans=0

# for i1,j1,i2,j2 in itertools.product(range(9),repeat=4):
#   # (i1,j1)から→↓の向きに(i2,j2)がある
#   if i2>i1 and j2>=j1 and S[i1][j1]=="#" and S[i2][j2]=="#":
#     di=i2-i1
#     dj=j2-j1
#     i3=i2+dj
#     j3=j2-di
#     i4=i3-di
#     j4=j3-dj
#     if 0<=i3<9 and 0<=j3<9 and 0<=i4<9 and 0<=j4<9 and S[i3][j3]=="#" and S[i4][j4]=="#":
#       ans+=1
# print(ans)
