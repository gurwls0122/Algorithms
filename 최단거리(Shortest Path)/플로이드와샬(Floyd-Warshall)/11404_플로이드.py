#https://www.acmicpc.net/problem/11404
import sys
n = int(sys.stdin.readline())
#최단경로를 구해야 하므로, 기본 값을 최대값 이상으로 함.
graph = [[1e9]* (n+1) for _ in range(n+1)]

m = int(sys.stdin.readline())

#시작도시와 도착도시가 같은 노선이 있으므로 최소값을 대입
for _ in range(m):
    a, b, c =map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

#플로이드와샬 알고리즘 실행
#k-> 경유 도시, i -> 시작 도시, j-> 도착 도시
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

#graph를 1부터 n+1까지로함. map과 lambda를 이용해 값 바꿔줌.
for row in graph[1:]:
    print(*list(map(lambda x: x if x!=1e9 else 0, row[1:])))