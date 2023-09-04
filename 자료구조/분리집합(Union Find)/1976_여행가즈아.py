#https://www.acmicpc.net/problem/1976
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = []

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(i):
        if lst[j] == 1:
            graph.append((i+1, j+1))

visit_lst = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a

if __name__ =="__main__":
    for a, b in graph:
        if find(a) == find(b):
            continue
        else:
            union(a, b)
    tmp = 0
    for i in range(M):
        if i==0:
            tmp = find(visit_lst[i])
        else:
            if tmp != find(visit_lst[i]):
                print("NO")
                exit()
    print("YES")