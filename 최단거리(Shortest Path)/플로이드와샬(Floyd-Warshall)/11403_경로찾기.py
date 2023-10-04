#https://www.acmicpc.net/problem/11403
import sys
N = int(sys.stdin.readline())
#그래프의 최대값이 10000이기 때문에 이보다큰 100000으로 최소값 설정
graph = [[10e5] * N for _ in range(N)]

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    #2차원 배열에 자신이 방문할 수 있는 노드까지 가능성을 1로 저장
    for j in range(N):
        if lst[j]:
            graph[i][j] = 1            
# print(graph)

#플로이드 와샬 알고리즘 사용
#k -> 경유지, i -> 출발지, j -> 도착지
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

#출력 구문
for i in range(N):
    for j in range(N):
        if graph[i][j] == 10e5:
            ans = 0
        else:
            ans = 1
        
        if j==N-1:
            print(ans)
        else:
            print(ans, end=" ")