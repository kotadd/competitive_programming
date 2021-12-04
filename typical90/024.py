# パリティを考える
# |b-a|はk以下である
# kが偶数ならaとbの偶奇が同じ
# kが奇数ならaとbの偶奇が違う

# aのsum - bのsum だと正しい結果にならない。
# aとbの個別の結果の差分を見ないと、a>b, b<aがわからないので

import sys


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = 0
    for i in range(n):
        d += abs(a[i] - b[i])

    if d <= k and (k - d) % 2 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
