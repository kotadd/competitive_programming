# 三角関数を使いこなそう
from math import pi, sin, cos, atan2, sqrt, degrees

import sys
input = sys.stdin.readline

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    e = int(input())

    theta = 2 * pi * e / T

    y = -L / 2 * sin(theta)
    z = L / 2 * (1 - cos(theta))

    d = sqrt(X**2 + (Y - y)**2)

    print(degrees(atan2(z, d)))
