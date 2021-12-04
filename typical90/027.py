# mapを使いこなそう
# pythonならdictかsetか
import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    d = dict()
    ans = []

    for i in range(1, n + 1):
        s = input()
        # if d.get(s) is None:
        if s not in d:
            d[s] = 1
            ans.append(i)

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
