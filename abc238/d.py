T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    if s == 0 and a == 0:
        print('Yes')
        continue
    x = a
    y = 0

    for i in reversed(range(60)):
        tmp = pow(2, i)
        if tmp > s:
            continue
        if x & tmp > 0:
            y += tmp
        elif x + y + tmp <= s:
            y += tmp
        if x + y == s and x & y == a:
            print('Yes')
            break
    else:
        print('No')
