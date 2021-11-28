# 参考：https://note.nkmk.me/python-union-find/
from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class UnionFind:
    def __init__(self, n):
        self.n = n
        # 要素数（値が負のときは根であり、数値がグループの要素数となる）
        self.root = [-1] * n

    # xが属するグループの根を求める（経路圧縮してrootを更新する）
    def find(self, x):
        stack = []
        while self.root[x] >= 0:
            stack.append(x)
            x = self.root[x]
        for i in stack:
            self.root[i] = x
        return x

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

        # union by size（xの方が小さい＝根になるようにする）
        if self.root[x] > self.root[y]:
            x, y = y, x

        self.root[x] += self.root[y]
        self.root[y] = x

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
        return [i for i, x in enumerate(self.root) if x < 0]

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
