# filter 関数の使い方
N, P = map(int, input().split())

A = list(map(int, input().split()))

ans = len(list(filter(lambda x: x < P, A)))

print(ans)
