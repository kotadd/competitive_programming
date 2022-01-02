# D - Cutting Woods
# https://atcoder.jp/contests/abc217/tasks/abc217_d
# 集合 S に x を追加
# S に属する x より大きい要素のうち最小の要素を取得
# S に属する x より小さい要素のうち最大の要素を取得
# => 順序付き集合（平衡二分探索木, B-Tree）


class BinaryTrie:
    def __init__(self, max_query=2 * 10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    def size(self):
        return self.cnt[0]

    # xの個数
    def count(self, x):
        pt = 0
        for i in range(self.bitlen - 1, -1, -1):
            y = x >> i & 1
            if self.nodes[2 * pt + y] == -1:
                return 0
            pt = self.nodes[2 * pt + y]
        return self.cnt[pt]

    # xの挿入
    def insert(self, x):
        pt = 0
        for i in range(self.bitlen - 1, -1, -1):
            y = x >> i & 1
            if self.nodes[2 * pt + y] == -1:
                self.id += 1
                self.nodes[2 * pt + y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2 * pt + y]
        self.cnt[pt] += 1

    # xの削除
    # xが存在しないときは何もしない
    def erase(self, x):
        if self.count(x) == 0:
            return
        pt = 0
        for i in range(self.bitlen - 1, -1, -1):
            y = x >> i & 1
            self.cnt[pt] -= 1
            pt = self.nodes[2 * pt + y]
        self.cnt[pt] -= 1

    # 昇順x番目の値(1-indexed)
    def kth_elm(self, x):
        assert 1 <= x <= self.size()
        pt, ans = 0, 0
        for i in range(self.bitlen - 1, -1, -1):
            ans <<= 1
            if self.nodes[2 * pt] != -1 and self.cnt[self.nodes[2 * pt]] > 0:
                if self.cnt[self.nodes[2 * pt]] >= x:
                    pt = self.nodes[2 * pt]
                else:
                    x -= self.cnt[self.nodes[2 * pt]]
                    pt = self.nodes[2 * pt + 1]
                    ans += 1
            else:
                pt = self.nodes[2 * pt + 1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か(1-indexed)
    # x以上の要素がない時はsize+1を返す
    def lower_bound(self, x):
        pt, ans = 0, 1
        for i in range(self.bitlen - 1, -1, -1):
            if pt == -1:
                break
            if x >> i & 1 and self.nodes[2 * pt] != -1:
                ans += self.cnt[self.nodes[2 * pt]]
            pt = self.nodes[2 * pt + (x >> i & 1)]
        return ans


b_tree = BinaryTrie()

L, Q = map(int, input().split())
b_tree.insert(0)
b_tree.insert(L)
for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        b_tree.insert(x)
    else:
        p = b_tree.lower_bound(x)
        print(b_tree.kth_elm(p) - b_tree.kth_elm(p - 1))
