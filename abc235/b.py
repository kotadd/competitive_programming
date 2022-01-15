N = int(input())
H = list(map(int, input().split()))

ans = 0
for h in H:
    if ans >= h:
        break
    ans = h

print(ans)
