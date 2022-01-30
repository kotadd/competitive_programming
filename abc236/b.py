N = int(input())
count = [4] * (N + 1)
A = list(map(int, input().split()))

for a in A:
    count[a] -= 1

for i in range(1, N + 1):
    if count[i] == 1:
        print(i)
        exit()
