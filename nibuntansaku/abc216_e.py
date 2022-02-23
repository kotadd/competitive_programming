# E - Amusement Park
# https://atcoder.jp/contests/abc216/tasks/abc216_e
# 二分探索 (or 貪欲法)
# アトラクションで遊ぶごとに楽しさが増え、そのアトラクションの楽しさが1下がる。

N, K = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= K:
    ans = 0
    for a in A:
        ans += a * (a + 1) // 2
    print(ans)
    exit()


def f(x):
    k = 0
    for a in A:
        k += max(0, a - x)
    return k <= K


# 自然数の和の公式を引き算して、t+1 ~ a までの和を出している
def calc_sum(a, t):
    return (a * (a + 1) // 2) - (t * (t + 1) // 2)


ng = 0
ok = 2 * 10**9 + 1

while ng + 1 < ok:
    m = (ok + ng) // 2
    if f(m):
        ok = m
    else:
        ng = m

x = ok
cur = 0
ans = 0
for a in A:
    ans += max(0, calc_sum(a, x))
    cur += max(0, a - x)

ans += ok * (K - cur)

print(ans)
