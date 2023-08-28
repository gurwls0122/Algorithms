#https://www.acmicpc.net/problem/1715
import sys
import heapq

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]

ans = 0

heapq.heapify(lst)

for _ in range(n-1, 0, -1):
    min_tmp = heapq.heappop(lst)
    min2_tmp = heapq.heappop(lst)
    ans += (min_tmp + min2_tmp)
    heapq.heappush(lst, min_tmp+min2_tmp)

print(ans)
