# https://atcoder.jp/contests/abc098/tasks/arc098_a
# 現状の向きの総和を先に求め、線形的にカウントしていく

N = int(input())
S = input()

ans = [S[1:N].count('E')]
for i in range(1, N):
    ans.append(ans[i - 1] - int(S[i] == "E") + int(S[i - 1] == "W"))

print(min(ans))
