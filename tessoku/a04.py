# A04 - Binary Representation 1
N = int(input())
ans = bin(N)[2:]
if len(ans) < 10:
    ans = '0' * (10 - len(ans)) + ans
print(ans)


# 回答
# 2進法の各位の値は、N/2**iの2で割った余りで求められる
# N/1 は Nの2進法表記の下0桁を削ったもの
# N/2 は Nの2進法表記の下1桁を削ったもの
# ...
N = int(input())
for i in reversed(range(10)):
    wari = 1 << i
    print(N // wari % 2, end='')
print()
