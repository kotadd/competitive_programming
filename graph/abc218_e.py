# E - Destruction
# https://atcoder.jp/contests/abc218/tasks/abc218_e
# クラスカル法

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
G = []
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G.append((c, (a, b)))

G.sort()

uf = UnionFind(N)

ans = 0
for i in range(M):
    a, b = G[i][1]
    if uf.issame(a, b):
        c = G[i][0]
        if c > 0:
            ans += c
        continue
    uf.unite(a, b)

print(ans)
