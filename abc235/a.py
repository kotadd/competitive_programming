a, b, c = input()
abc = a + b + c
bca = b + c + a
cab = c + a + b
ans = int(abc) + int(bca) + int(cab)
print(ans)

# 別解
a, b, c = input()
s = int(a) + int(b) + int(c)
print(111 * s)
