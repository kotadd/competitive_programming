# 同じ意味のものをまとめて考える
import sys
input = sys.stdin.readline

n = int(input())

A = list(map(lambda x: int(x) % 46, input().split()))
B = list(map(lambda x: int(x) % 46, input().split()))
C = list(map(lambda x: int(x) % 46, input().split()))


def count_num_in_dict(X):
    x_dict = dict()
    for x in X:
        if x_dict.get(x):
            x_dict[x] += 1
        else:
            x_dict[x] = 1
    return x_dict


a_dict = count_num_in_dict(A)
b_dict = count_num_in_dict(B)
c_dict = count_num_in_dict(C)

total = 0
for ka, va in a_dict.items():
    for kb, vb in b_dict.items():
        for kc, vc in c_dict.items():
            if (int(ka) + int(kb) + int(kc)) % 46 == 0:
                total += va * vb * vc

print(total)
