# 解説
# https://atcoder.jp/contests/abc180/editorial/181
# 「d が N の約数である」ことと「N/d が N の約数である」ことは同値
# d*d <= N までの間に N% d == 0の時、dとN/dを両方追加していけば良い
# 約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
print(*make_divisors(N), sep="\n")
