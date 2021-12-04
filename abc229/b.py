A, B = input().split()

A = A[::-1]
B = B[::-1]

N = min(len(A), len(B))

for i in range(N):
    a = int(A[i])
    b = int(B[i])

    if a + b >= 10:
        print('Hard')
        exit()

print('Easy')
