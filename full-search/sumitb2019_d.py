N = int(input())
S = input()
ones = set()
twos = set()
threes = set()

ans = 0
for c in S:
    for item in twos:
        threes.add(item + c)
    for item in ones:
        twos.add(item + c)
    ones.add(c)

print(len(threes))

# listを使う場合
# A1 = [False] * 10
# A2 = [False] * 100
# A3 = [False] * 1000
# for c in S:
#     for i, a in enumerate(A2):
#         A3[i*10+c] |= a
#     for i, a in enumerate(A1):
#         A2[i*10+c] |= a
#     A1[c] = True
# print(sum(A3))
