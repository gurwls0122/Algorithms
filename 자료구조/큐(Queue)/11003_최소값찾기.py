#https://www.acmicpc.net/problem/11003
import sys
from collections import deque
N, L = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
queue = deque([(lst[0], 0)])
print(queue[0][0], end=" ")

for i in range(1, N):
    # print(queue)
    while queue and queue[-1][0]>lst[i]:
        queue.pop()

    while queue and queue[0][1]<i-L+1:
        queue.popleft()

    queue.append((lst[i], i))

    print(queue[0][0], end=" ")