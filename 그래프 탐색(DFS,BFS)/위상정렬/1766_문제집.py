#https://www.acmicpc.net/problem/1766
import sys
from collections import defaultdict
import heapq

N, M = map(int, sys.stdin.readline().split())
dic = defaultdict(list)

#위상정렬을 사용하기 위해 진입차수를 indegree로 설정
indegree = [0]*(N+1)
#방문해야되는 순서가 정해져있으므로(오름차순) priority queue사용
p_queue = []
#정답을 저장할 배열
ans = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    #입력이 들어오면 자신이 나오게 된다면 선행되는 수를 dic에 저장해줌
    dic[a].append(b)
    #선행되는 수는 하나의 진입차수가 늘어남
    indegree[b] +=1

#진입차수를 확인하며 진입차수가 0인 값을 priority queue에 삽입
for i in range(1, N+1):
    if indegree[i] == 0:
        p_queue.append(i)
    else:
        continue
#우선순위큐사용
heapq.heapify(p_queue)

#우선순위큐가 빌때까지
while p_queue:
    #우선순위큐에서 가장 작은값을 pop해주고
    ans.append(val:=heapq.heappop(p_queue))

    #해당 값을 우선순위로 가지는 값들을 찾아서
    for i in dic[val]:
        #진입차수를 1만큼 낮추고
        indegree[i] -=1
        #진입차수가 0이 되었다면 heapq에 해당 index를 넣어줌
        if indegree[i] == 0:
            heapq.heappush(p_queue, i)

print(*ans)