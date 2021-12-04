s1 = input()
s2 = input()

c1 = s1.count('#')
c2 = s2.count('#')

if c1 == 0 or c2 == 0:
    print('Yes')
elif c1 + c2 >= 3:
    print('Yes')
else:
    print('No')
