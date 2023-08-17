import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

prefix_sum = []
for i in range(N):
    if i==0:
        prefix_sum.append(lst[i])
    else:
        prefix_sum.append(lst[i] + prefix_sum[i-1])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i==1:
        print(prefix_sum[j-1])
    else:
        print(prefix_sum[j-1] - prefix_sum[i-2])