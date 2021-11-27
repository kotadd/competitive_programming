import sys
input = sys.stdin.readline

N = 5  # Nは0/1となる対象の数

for i in range(2**N):
    switches = [0] * N
    for j in range(N):
        if ((i >> j) & 1):
            switches[N - 1 - j] = 1
    print(switches)
