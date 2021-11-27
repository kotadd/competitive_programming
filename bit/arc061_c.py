S = input()
N = len(S) - 1
ans = 0

# 例：123
# 演算子が入るのは 2**2 = 4通り

# 0 0：123
# 0 1：1+23
# 1 0：12+3
# 1 1：1+2+3

# i = 0, 1, 2, 3
for i in range(1 << N):
    k = 0
    # j = 0,1
    for j in range(N):
        # 2 ** 0 = 1 ：1と2の間に演算子フラグがついているか
        # 2 ** 1 = 2 ：2と3の間に演算子フラグがついているか
        if i & (1 << j):
            ans += int(S[k:(j + 1)])
            k = j + 1
    ans += int(S[k:])
    # print(ans)

print(ans)
