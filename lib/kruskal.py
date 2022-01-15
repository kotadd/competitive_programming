# クラスカル法
# 1: 辺集合 edges を (w, (u,v)) のtupleで保持する。
# w: 重み u,v: 辺
# 2: edgesを昇順にソート
# 3: 重みの小さい順に確認し、UnionFindを利用して、サイクルが形成されないなら追加するというのを繰り返す

from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n

    def find(self, x):
        stack = []
        while self.root[x] >= 0:
            stack.append(x)
            x = self.root[x]
        for i in stack:
            self.root[i] = x
        return x

    def issame(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x
        return True

    def size(self, x):
        return -self.root[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(
            f'{r}: {m}' for r,
            m in self.all_group_members().items())


N, M = map(int, input().split())

# 1: 辺集合 edges を (w, (u,v)) のtupleで保持する。
edges = []

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((c, (a, b)))

# 2: edgesを昇順にソート
edges.sort()

# 3: 重みの小さい順に確認し、UnionFindを利用して、サイクルが形成されないなら追加するというのを繰り返す
uf = UnionFind(N)
ans = 0
for e in edges:
    w = e[0]
    u = e[1][0]
    v = e[1][1]

    if uf.issame(u, v):
        continue

    ans += w
    uf.unite(u, v)

# MST（Minimum Spanning Tree：最小全域木）のコスト
print(ans)
