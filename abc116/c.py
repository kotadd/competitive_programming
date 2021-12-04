# C - Grand Garden
# https://atcoder.jp/contests/abc116/tasks/abc116_c

N = int(input())
H = list(map(int, input().split())) + [0]

ans = 0
tmp = 0
for i in range(1, N + 1):
    # 減少した時、前の花に個別に水を与えないといけないのでansに追加
    if H[i] < H[i - 1]:
        ans += H[i - 1] - H[i]
        tmp = H[i]
    # 増加していくときは全体に水を与えられるので、そのまま追加
    else:
        tmp = H[i]

print(ans)
