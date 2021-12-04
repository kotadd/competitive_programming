# D - Querying Multiset
# https://atcoder.jp/contests/abc212/tasks/abc212_d
# heapq：優先度付きキューを知っているかどうか

import heapq
Q = int(input())

ans = []
offset = 0
pick = 0
for i in range(Q):
    query = input()
    if query[0] == '1':
        x = int(query[2:])
        # 追加時は（配列, 入れる値）
        heapq.heappush(ans, x - offset)
    elif query[0] == '2':
        x = int(query[2:])
        offset += x
    else:
        # heappopは最小の値を取得して削除する
        print(heapq.heappop(ans) + offset)
