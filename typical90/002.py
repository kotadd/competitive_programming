# 小さい制約は全探索を考えよう
n = int(input())

if n % 2 == 1:
    exit(0)

array = []
for i in range(2 ** n):
    res = ["("] * n
    for j in range(n):
        if i >> j & 1:
            res[n - 1 - j] = ")"

    array.append(res)

ans = []
for i in range(len(array)):
    res = array[i]
    count = 0
    for j in range(n):
        if res[j] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        ans.append(res)

for arr in ans:
    print(*arr, sep="")
