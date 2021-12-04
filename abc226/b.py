N = int(input())

L = set()
for i in range(N):
    x = input()
    L.add(x)

print(len(L))

# A = set()
# for i in range(N):
#     _, *a = map(int, input().split())
#     A.add(tuple(a))

# print(len(A))


# print(len(set(input() for _ in range(N))))
