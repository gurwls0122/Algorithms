#https://www.acmicpc.net/problem/11000
import sys
import heapq

n = int(sys.stdin.readline())
#강의 시작시간을 기준으로 sorting
lst = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)] , key=lambda x: x[0])

#강의 종료시간을 기준으로 우선순위큐를 생성한다
#이유 : 시작시간이 이른 순서대로 정렬된 리스트를 탐색할 것이며, 종료시간을 우선순위큐에 넣어 시작시간보다 종료시간이 늦다면 강의실을 새로 배정해주면 되기 떄문!
queue = [lst[0][1]]
heapq.heapify(queue)

for i in range(1, n):
    #종료시간을 우선순위큐에 넣어 시작시간보다 종료시간이 늦다면 강의실을 새로 배정해주고 강의 종료시간을 우선순위큐에 넣어줌
    if lst[i][0] < queue[0]:
        heapq.heappush(queue, lst[i][1])
    #종료시간이 시작시간보다 빠르다면 pop과 동시에 push
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, lst[i][1])

print(len(queue))