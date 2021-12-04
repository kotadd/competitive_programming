# https://atcoder.jp/contests/abc169/tasks/abc169_c

# 浮動小数点の誤差を無視でき、人の計算結果により近い（正確さの高い）値を導ける
# import decimal
# a, b = map(decimal.Decimal, input().split())
# print(a * b // 1)


# 四捨五入する
# a, b = input().split()
# a = int(a)
# b = round(float(b) * 100)
# print(a * b // 100)

# periodで区切って誤差を消す
a, b = input().split()
a = int(a)
b1, b2 = b.split('.')
answer = a * (int(b1) * 100 + int(b2))
print(answer // 100)
