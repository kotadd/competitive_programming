# E - Sequence Sum
# https://atcoder.jp/contests/abc179/tasks/abc179_e
# X^2をN回繰り返す中で表れた数をMで割った余りの和
# Mが高々 10^5 までなので、繰り返しの数が表れたタイミングで末端まで計算すれば良い

N, X, M = map(int, input().split())

ans = X
d = {X: 0}
rui = [0, X]

x = X
for i in range(1, N):
    x = pow(x, 2, M)
    if x == 0:
        ans = rui[-1]
        break
    elif x in d:
        l = len(rui) - d[x] - 1
        val = rui[-1] - rui[d[x]]
        diff = (N - i) // l
        ans += val * diff
        i += diff * l
        ans += rui[d[x] + N - i] - rui[d[x]]
        break
    else:
        rui.append(rui[-1] + x)
        d[x] = i
        ans += x

print(ans)
