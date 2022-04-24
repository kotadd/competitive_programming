# C - Just K
# https://atcoder.jp/contests/abc249/tasks/abc249_c
# bit全探索: 同じ文字のカウント
N, K = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

lst = ['abcdefghijklmnopqrstuvwxyz']
ans = 0
for i in range(1 << N):
    tmp = ''
    for j in range(N):
        if i & (1 << j):
            tmp += S[j]

    cnt = 0
    for x in lst:
        if tmp.count(x) == K:
            cnt += 1
    ans = max(ans, cnt)

print(ans)


# 別解 https://atcoder.jp/contests/abc249/submissions/31175960
# n, k = map(int, input().split())

# S = [input() for _ in range(n)]
# ans = 0
# for bit in range(1 << n):
#     cnt = [0] * 26
#     for i in range(n):
#         if bit >> i & 1:
#             for s in S[i]:
#                 cnt[ord(s) - 97] += 1
#     ans = max(ans, cnt.count(k))
# print(ans)
