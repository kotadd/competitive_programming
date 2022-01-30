# D - Sum of Divisors
# https://atcoder.jp/contests/abc172/tasks/abc172_d
# Xまでの、(正の約数の個数 × X) の総和

N = int(input())


# エラトステネスっぽく
def solve(N: int):
    divs = [1] * (N + 1)
    for p in range(1, N + 1):
        q = p * 2
        while q <= N:
            divs[q] += 1
            q += p
    return divs


divs = solve(N)
ans = 0

for i in range(1, N + 1):
    ans += divs[i] * i

print(ans)
