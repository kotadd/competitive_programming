N = int(input())
S = input()

ans = 0
tmp = 0
for i in range(1, N):
    if S[i] == S[i - 1]:
        tmp += 1
    else:
        ans += sum(range(tmp + 1))
        tmp = 0

ans += sum(range(tmp + 1))
print(ans)
