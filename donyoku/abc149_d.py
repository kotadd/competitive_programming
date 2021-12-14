# D - Prediction and Restriction
# https://atcoder.jp/contests/abc149/tasks/abc149_d
# 貪欲法（DPでも解ける）
# じゃんけんで勝利したときのポイントの最大化
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
counted = [0] * N
ans = 0


def hand_to_point(s: str):
    if s == 'r':
        return P
    elif s == 's':
        return R
    return S


for i in range(N):
    hand = T[i]
    if i - K >= 0:
        pre_hand = T[i - K]
        if hand != pre_hand:
            ans += hand_to_point(hand)
            counted[i] = 1
        else:
            if counted[i - K] == 0:
                ans += hand_to_point(hand)
                counted[i] = 1
    else:
        ans += hand_to_point(hand)
        counted[i] = 1

print(ans)
