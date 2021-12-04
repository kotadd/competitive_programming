def findSumOfDigits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def main():
    n, a, b = map(int, input().split())
    total = 0

    for i in range(n + 1):
        val = i
        t = findSumOfDigits(val)
        if a <= t <= b:
            total += i
    print(total)


if __name__ == '__main__':
    main()
