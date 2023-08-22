import sys
from collections import defaultdict
import heapq
V, E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [False] * (V+1)

for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

def prim(node):
    ans = 0
    visited[node] = True
    candidate = graph[node]
    heapq.heapify(candidate)

    while candidate:
        cost, near_node = heapq.heappop(candidate)
        # print(cost, near_node)
        if visited[near_node] == True:
            continue
        else:
            visited[near_node] = True
            ans+=cost
            for i in graph[near_node]:
                if not visited[i[1]]:
                    heapq.heappush(candidate, i)
    
    return ans
if __name__ =="__main__":
    print(prim(1))
