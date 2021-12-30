#  C - Tsundoku
# https://atcoder.jp/contests/abc172/tasks/abc172_c
# 累積和

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rui_a = [0]
rui_b = [0]

for i in range(N):
    rui_a.append(rui_a[i] + A[i])

for i in range(M):
    rui_b.append(rui_b[i] + B[i])

ans = 0
j = M
for i in range(N + 1):
    if rui_a[i] > K:
        break
    while rui_b[j] > K - rui_a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
