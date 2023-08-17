#https://www.acmicpc.net/problem/1697
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [False] * (max(N, K)*2 + 1)

def bfs(start, end):
    queue = deque([(start, 0)])

    while queue:
        node, depth = queue.popleft()
        visited[node] = True
        if node == end:
            print(depth)
            break
        else:
            # print(node)
            max_val = max(N, K)*2
            if node + 1 <= max_val and not visited[node+1]:
                queue.append((node+1, depth+1))
            if node - 1 >= 0 and not visited[node-1]:
                queue.append((node-1, depth+1))
            if node*2 <= max_val and not visited[node*2]:
                queue.append((node*2, depth+1))

if __name__ == "__main__":
    bfs(N, K)
