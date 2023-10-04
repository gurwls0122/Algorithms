#https://www.acmicpc.net/problem/1753
import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
#노드의 개수 +1 만큼 선언
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

#거리 값 초기화
distance = [10e9] * (V+1)

#다익스트라 진행
def dijkstra(start):
    #heapq로 이용할 queue선언
    queue = []
    #시작 노드의 거리는 0 초기화
    distance[start] = 0
    #heapq에 시작 노드의 거리와 노드 번호 추가
    heapq.heappush(queue, (0, start))

    #queue가 빌때까지 반복하면서
    while queue:
        dist, node = heapq.heappop(queue)
        #만약, 저장되어있는 distance값이 현재 가져온 값보다 좋을 경우 넘어감(중복 체크)
        if distance[node] < dist:
            continue
        #그 외의 경우
        else:
            #각 node로 부터 이어져있는 다음 node들을 확인한 후
            for next_node, next_dis in graph[node]:
                #"시작점부터 현재 노드의 거리 + 다음 노드 까지의 거리"가 "저장되어있는 다음 노드의 최단거리" 보다 작다면 queue에 추가
                if next_dis +dist < distance[next_node]:
                    distance[next_node] = next_dis + dist
                    heapq.heappush(queue, (dist+next_dis, next_node))
    
    # print(distance)

if __name__ =="__main__":
    dijkstra(start)
    for i in range(1, V+1):
        if distance[i] == 10e9:
            print("INF")
        else:
            print(distance[i])