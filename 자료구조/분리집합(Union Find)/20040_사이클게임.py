#https://www.acmicpc.net/problem/20040
import sys
n, m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

if __name__ == "__main__":
    cnt = 0
    for a, b in lst:
        cnt +=1
        if find(a) == find(b):
            print(cnt)
            exit(0)
        else:
            union(a, b)
    
    print(0)