# Swiss-System Tournament

N, M = map(int, input().split())

hands = [input() for _ in range(2 * N)]
# i 位の人の勝数と番号
rank = [[0, i] for i in range(2 * N)]


# じゃんけん
def judge(a, b):
    # 引き分けなら-1,前者勝ちなら0,後者勝ちなら1
    if a == b:
        return -1
    if a == 'G' and b == 'C':
        return 0
    if a == 'C' and b == 'P':
        return 0
    if a == 'P' and b == 'G':
        return 0
    return 1


for j in range(M):
    for i in range(N):
        # playerの番号
        player1 = rank[2 * i][1]
        player2 = rank[2 * i + 1][1]
        result = judge(hands[player1][j], hands[player2][j])
        if result != -1:
            rank[2 * i + result][0] += 1

    # 勝ち数で降順、番号は昇順にする
    rank.sort(key=lambda x: (x[0], -x[1]), reverse=True)

for _, i in rank:
    print(i + 1)
