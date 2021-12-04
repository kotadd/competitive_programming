import sys
input = sys.stdin.readline

N = int(input())

X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

count = 0
for i in range(N):
    for j in range(i, N):
        if X[i] == X[j] and Y[i] == Y[j]:
            continue
        for k in range(j, N):
            if X[j] == X[k] and Y[j] == Y[k]:
                continue
            if X[k] != X[j] and X[j] != X[i]:
                a1 = (Y[k] - Y[j]) / (X[k] - X[j])
                a2 = (Y[j] - Y[i]) / (X[j] - X[i])
                if a1 == a2:
                    continue
            if X[k] == X[j] == X[i] or Y[k] == Y[j] == Y[i]:
                continue

            count += 1

print(count)
