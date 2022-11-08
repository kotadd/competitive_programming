# C - XX to XXX
# https://atcoder.jp/contests/abc259/tasks/abc259_c
# ランレングス圧縮 連長圧縮

S = input()
T = input()


def RLE(S):
    ret = []
    crr = S[0]
    cnt = 0
    for c in S:
        if crr == c:
            cnt += 1
        else:
            ret.append((crr, cnt))
            crr = c
            cnt = 1
    ret.append((crr, cnt))
    return ret


s = RLE(S)
t = RLE(T)

if len(s) != len(t):
    print("No")
    exit()

for (x, a), (y, b) in zip(s, t):
    if not (x == y and (a == b or (a >= 2 and a <= b))):
        print("No")
        exit()

print("Yes")
