from collections import defaultdict
a = input()
b = input()

d_a = defaultdict(int)
d_b = defaultdict(int)
for i in range(len(a)):
    d_a[int(a[i])] += 1

for i in range(len(b)):
    d_b[int(b[i])] += 1

ans_a = ''
ans_b = ''

flag = False
for i in reversed(range(1, 10)):
    if flag:
        break
    for j in reversed(range(1, 10)):
        if i + j == 10 and i in d_a and j in d_b:
            ans_a = str(i)
            ans_b = str(j)
            d_a[i] -= 1
            d_b[j] -= 1
            flag = True
            break

if len(ans_a) == 1:
    for i in reversed(range(1, 10)):
        for j in reversed(range(1, 10)):
            if i + j == 9 and i in d_a and j in d_b:
                n = min(d_a[i], d_b[j])
                ans_a += str(i) * n
                ans_b += str(j) * n
                d_a[i] -= n
                d_b[j] -= n

for i in reversed(range(1, 10)):
    if i in d_a:
        ans_a += str(i) * d_a[i]
        d_a[i] = 0

for i in reversed(range(1, 10)):
    if i in d_b:
        ans_b += str(i) * d_b[i]
        d_b[i] = 0

print(ans_a[::-1])
print(ans_b[::-1])
