# オーバーフローに注意（pythonは気にせず計算できる）

# lcm（最小公倍数）はpython3.9からなので、Atcoderで使えない

# from math import lcm
# import sys
# input = sys.stdin.readline

# a, b = map(int, input().split())

# ans = lcm(a, b)
# print(ans if ans <= 10**18 else 'Large')


from math import gcd
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

ans = a * b // gcd(a, b)
if ans > 10**18:
    print('Large')
else:
    print(ans)
