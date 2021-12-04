# B - Substring
# 最長部分文字列 （S in Tを使わない）
# https://atcoder.jp/contests/abc177/tasks/abc177_b

S = input()
T = input()

N = len(S) - len(T) + 1
ans = len(T)

for i in range(N):
    diff = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            diff += 1
    ans = min(ans, diff)
print(ans)
