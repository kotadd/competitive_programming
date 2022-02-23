def judge():
    S = input()

    la = len(S) - len(S.lstrip('a'))
    ra = len(S) - len(S.rstrip('a'))

    if la > ra:
        return False
    T = 'a' * (ra - la) + S
    return T == T[::-1]


print('Yes' if judge() else 'No')
