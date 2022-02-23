H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
# 転置行列にする処理
At = list(zip(*A))
for r in At:
    print(*r)
