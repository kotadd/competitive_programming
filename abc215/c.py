from itertools import permutations

S, K = input().split()
K = int(K)

ans = set()
for v in permutations(S):
    ans.add("".join(v))

ans = sorted(ans)
print(ans[K - 1])
