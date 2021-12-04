# コーナーケースに気をつけよう

import sys
from math import ceil


def main():
    input = sys.stdin.readline
    h, w = map(int, input().split())

    # if h == 1 or w == 1:
    if min(h, w) == 1:
        print(h * w)
    else:
        print(ceil(h / 2) * ceil(w / 2))

        # ビットをシフトさせることによって、ceilと同じことができる
        # h = (h + 1) >> 1
        # w = (w + 1) >> 1
        # print(h * w)


if __name__ == '__main__':
    main()
