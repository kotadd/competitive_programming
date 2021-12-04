# 整数で処理して誤差を無くそう
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

print('Yes' if a < c**b else 'No')
