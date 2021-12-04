# https://atcoder.jp/contests/typical90/tasks/typical90_bo
# N進法展開を理解しよう
n, k = input().split()
k = int(k)

if n == '0':
    print(0)
    exit(0)

for _ in range(k):
    # 八進法の整数nを10進法に直す
    # int("21", base=8) => 17
    n = int(n, 8)
    array = []
    while n:
        if n % 9 == 8:
            array.append(5)
        else:
            array.append(n % 9)
        n //= 9
    n = ''.join(map(str, reversed(array)))

print(n)
