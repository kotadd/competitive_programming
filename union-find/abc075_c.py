from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


# Union-Find
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    # xが属するグループの根を求める
    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    # xとyが同じグループに属するかどうか（根が一致するかどうか）
    def issame(self, x, y):
        return self.find(x) == self.find(y)

    # xを含むグループとyを含むグループを併合する
    def unite(self, x, y):

        # xとyをそれぞれ根まで移動する
        x = self.find(x)
        y = self.find(y)

        # すでに同じグループのときは何もしない
        if x == y:
            return False

        # union by size（y側のサイズが小さくなるようにする）
        if self.rank[x] < self.rank[y]:
            x, y = y, x

        # yをxの子とする
        self.root[y] = x
        self.rank[x] += self.rank[y]

        return True

    # xを含むグループのサイズ
    def size(self, x):
        return -self.root[self.find(x)]

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(
            f'{r}: {m}' for r,
            m in self.all_group_members().items())


N, M = map(int, input().split())
es = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    es.append((a, b))

ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i != j:
            a, b = es[j]
            uf.unite(a, b)

    a, b = es[i]
    if uf.unite(a, b):
        ans += 1

print(ans)
