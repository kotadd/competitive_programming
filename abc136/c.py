# C - Build Stairs
# https://atcoder.jp/contests/abc136/tasks/abc136_c
N = int(input())
H = list(map(int, input().split()))[::-1]

ans = 'Yes'
for i in range(N - 1):
    if H[i + 1] - H[i] >= 2:
        ans = 'No'
    elif H[i + 1] - H[i] == 1:
        H[i + 1] -= 1

print(ans)
