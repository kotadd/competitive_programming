S = list(input())
a, b = map(int, input().split())
a -= 1
b -= 1
S[a], S[b] = S[b], S[a]

print(*S, sep="")
