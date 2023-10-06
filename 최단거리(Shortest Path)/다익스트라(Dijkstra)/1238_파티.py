#https://www.acmicpc.net/problem/1238
import sys
import heapq
N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
max_ans = 0

#graph에 저장될때 : (거리, 도착점)
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append([t, b])

#총거리 저장 리스트
total_dist = [0] * (N+1)

#다익스트라 알고리즘 -> 입력인자 시작 노드
def dijkstra(start):
    #각 시작 노드별 거리를 저장할 리스트
    distance = [1e9] * (N+1)
    
    #각 노드별 거리를 우선순위 큐에 넣어서 확인
    queue = []
    
    #시작 노드의 거리는 0으로 초기화
    distance[start] = 0
    
    #heapq에 시작 노드를 추가
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        #만약, 현재 노드로부터 도착지점까지의 거리가 나오고 해당 노드가 도착 노드가 아닐때
        if start!=X and node==X:
            #총 거리에 구한 거리를 추가해줌
            total_dist[start] += distance[X]
            # print(start, distance)
            break
        
        #노드의 중복 확인
        if dist > distance[node]:
            continue
        else:
            #현재 노드로부터 이어져있는 값 추가
            for new_dist, new_node in graph[node]:
                if distance[new_node] > dist+new_dist:
                    distance[new_node] = dist+new_dist
                    heapq.heappush(queue, (dist+new_dist, new_node))
    #만약, 시작노드가 도착 노드와 같다면
    #도착노드로부터 다른 노드까지 걸리는 모든 시간을 더해줘야 하는 로직
    if start ==X:
        for i in range(1, N+1):
            total_dist[i] += distance[i]

for i in range(1, N+1):
    dijkstra(i)

print(max(total_dist[1:]))
