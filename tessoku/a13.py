# A13 - Close Pairs
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# しゃくとり法
N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0] * N
j = 1
for i in range(N):
    while j != N and A[j] - A[i] <= K:
        j += 1
        if j == N:
            break
    R[i] = j - i - 1
print(sum(R))


# 二分探索
# import bisect

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N):
#     ans += bisect.bisect_left(A, A[i] + K + 1) - i - 1

# print(ans)
