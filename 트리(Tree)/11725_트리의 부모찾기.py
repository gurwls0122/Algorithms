#https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10**6)
tree = {}
N = int(sys.stdin.readline())
for i in range(1, N+1):
    tree[i] = []

for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

visited = [False] * N
ans = [0]*(N+1)

def dfs(node, parent):
    if visited[node-1] == False:
        visited[node-1] = True
        ans[node] = parent
        for i in tree[node]:
            dfs(i, node)
    
if __name__ =="__main__":
    dfs(1,0)
    for i in range(2, N+1):
        print(ans[i])