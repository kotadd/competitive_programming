X = input()

ans = '9' * len(X)
for c0 in range(1, 10):
    for d in range(-9, 9):
        end = c0 + d * (len(X) - 1)
        if end >= 10 or end < 0:
            continue
        s = ''
        for k in range(len(X)):
            s += str(c0 + d * k)
        if s >= X:
            ans = min(ans, s)
print(ans)
