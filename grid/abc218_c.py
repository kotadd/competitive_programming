# https://atcoder.jp/contests/abc218/tasks/abc218_c
# グリッドを読み込み、90度回転と平行移動で一致するか

N = int(input())


# グリッドを読み込んで#の位置の集合を返す
def read():
    S = set()
    for y in range(N):
        l = input()
        for x in range(N):
            if l[x] == "#":
                S.add((x, y))
    return S


S = read()
T = read()

for _ in range(4):
    # 最も左（複数あればそのうちで最も上）の#を(0, 0)の位置にする
    mx, my = min(S)
    S = set((x - mx, y - my) for x, y in S)
    mx, my = min(T)
    T = set((x - mx, y - my) for x, y in T)

    if S == T:
        print('Yes')
        exit()

    # Tを回転
    T = set((y, -x) for x, y in T)

print('No')
