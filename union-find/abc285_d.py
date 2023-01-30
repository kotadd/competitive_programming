# D - Change Usernames
# https://atcoder.jp/contests/abc285/tasks/abc285_d
# UnionFind
# グラフにサイクルが存在するかを判定する

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


N = int(input())
se = {}
uf = UnionFind(N * 2)

for _ in range(N):
    s, t = input().split()
    if s in se:
        u = se[s]
    else:
        u = len(se)
        se[s] = u

    if t in se:
        v = se[t]
    else:
        v = len(se)
        se[t] = v
    if uf.issame(u, v):
        print('No')
        exit()
    uf.unite(u, v)

print('Yes')
