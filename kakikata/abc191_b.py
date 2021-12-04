# B - Remove It
N, X = map(int, input().split())
A = list(map(int, input().split()))

# for 文で回した結果を横に並べたいとき
print(" ".join([str(i) for i in A if i != X]))
