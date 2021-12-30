S = input()
T = input()

se = set()
for s, t in zip(S, T):
    se.add((ord(s) - ord(t)) % 26)

if len(se) == 1:
    print('Yes')
else:
    print('No')
