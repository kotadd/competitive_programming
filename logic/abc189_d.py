# D - Logical Expression
# https://atcoder.jp/contests/abc189/tasks/abc189_d
# 制約が60なのでbit全探索はできない
# 具体的に記述して規則を探す
# ANDは数字が一位に決まるため、
# ORの箇所ごとに 2**(i+1) を加算していけば良い
N = int(input())
S = [input() for _ in range(N)]

ans = 1
for i in range(N):
    if S[i] == 'OR':
        ans += 2**(i + 1)
print(ans)
