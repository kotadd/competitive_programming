N = input()

zeros = ''
for _ in range(4 - len(N)):
    zeros += '0'

print(zeros + N)
