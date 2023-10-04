#https://www.acmicpc.net/problem/1956
import sys
V, E = map(int,sys.stdin.readline().split())
graph = [[10e9]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, dist = map(int, sys.stdin.readline().split())
    graph[a][b] = dist

#플로이드 와샬 알고리즘을 이용
#k -> 경유지, i -> 시작지, j -> 도착지
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = 10e9
for i in range(1, V+1):
    ans = min(ans, graph[i][i])

if ans == 10e9:
    print(-1)
else:
    print(ans)