# ABC 087
N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

candies = [sum(A1[0: i + 1]) + sum(A2[i:]) for i in range(N)]

print(max(candies))


# print(f'A1: {A1}')
# print(f'A2: {A2}')

# i = 0
# 3 + 5 + 3 + ... = 26

# i = 1
# 3+3+3+4+4+2+3+2 = 24
