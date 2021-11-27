S = input()
N = len(S) - 1

# 3箇所なので iは2**3 = 8通り
for i in range(1 << N):
    ops_list = ['-'] * N
    for j in range(N):
        if i & (1 << j):
            ops_list[j] = '+'

    ans = S[0]
    total = int(S[0])
    for j in range(N):
        if ops_list[j] == '+':
            total += int(S[j + 1])
            ans += '+' + S[j + 1]
        else:
            total -= int(S[j + 1])
            ans += '-' + S[j + 1]

    if total == 7:
        print(ans + '=7')
        exit()
