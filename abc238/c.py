MOD = 998244353
N = input()

digit = len(N)
if digit == 1:
    n = int(N)
    print(n * (n + 1) // 2)
    exit()

x = int((digit - 1) * '9')

n = int(N) - x
ans = n * (n + 1) // 2 % MOD

digit -= 1
while digit > 0:
    if digit == 1:
        ans += 45
        ans %= MOD
        break
    n = 9**digit
    ans += n * (n + 1) // 2
    ans %= MOD
    digit -= 1

print(ans)
