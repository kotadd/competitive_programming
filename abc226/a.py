a, b = input().split('.')
a = int(a)
if int(b[0]) >= 5:
    print(a + 1)
else:
    print(a)


# 解法2：Pythonでそのままroundを利用すると、0.5に対する丸めに失敗するため、小さな数値を足すなどが必要
# x=float(input())
# print(int(round(x+0.0005,0)))

# 解法3：decimalライブラリを利用して下記のように解くことも可能
# https://note.nkmk.me/python-round-decimal-quantize/
# from decimal import Decimal, ROUND_HALF_UP
# print(Decimal(str(input())).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
