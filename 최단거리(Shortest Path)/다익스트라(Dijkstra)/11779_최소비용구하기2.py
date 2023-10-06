#https://www.acmicpc.net/problem/11779
import sys
import heapq
import copy
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])

#출발지, 도착지
start, end = map(int, sys.stdin.readline().split())

#시작점으로부터 거리를 저장해놓을 함수
distance = [1e9] * (n+1)

def dijkstra(start):
    distance[start] = 0
    queue = []
    #queue에 시작점으로부터의 거리, 시작점, 현재까지 지나온 경로 추가
    heapq.heappush(queue, [0, start, [start]])

    while queue:
        dist, node, path = heapq.heappop(queue)
        #만약, 도착점이 pop됐다면 현재까지 지나온 경로를 출력        
        if node == end:
            return path
        #중복 방지
        if dist > distance[node]:
            continue
        else:
            #현재 노드로 부터 이어져있는 다음 노드 검사
            for new_dist, new_node in graph[node]:
                #다음 노드에 저장되어있는 거리 값이 현재 노드를 포함한 거리값보다 크다면
                if dist+new_dist < distance[new_node]:
                    #거리 최신화
                    distance[new_node] = dist+new_dist
                    #경로에 현재 노드를 다음 노드를 추가해주고
                    path.append(new_node)
                    #새로운 경로를 새로운 리스트에 넣어서
                    new_path = copy.deepcopy(path)
                    #heapq에 추가
                    heapq.heappush(queue, [dist+new_dist, new_node, new_path])
                    #경로는 유지되어야 하므로 pop
                    path.pop()

if __name__=="__main__":
    ans = dijkstra(start)
    print(distance[end])
    print(len(ans))
    print(*ans)