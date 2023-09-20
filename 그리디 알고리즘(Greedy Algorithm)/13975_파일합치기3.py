#https://www.acmicpc.net/problem/13975
import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    p_queue = list(map(int, sys.stdin.readline().split()))
    #입력받은 list를 priority queue로 선언
    heapq.heapify(p_queue)
    ans = 0

    while p_queue:
        #priority queue의 원소가 한개라면(모든 값이 더해졌다면) 멈춤
        if len(p_queue) == 1:
            print(ans)
            break
        #priority queue에서 가장 작은 값을 두개 꺼내서
        min_1 = heapq.heappop(p_queue)
        min_2 = heapq.heappop(p_queue)
        #그 값을 더해서 최종 값에 더해주고
        ans +=min_1+min_2
        #더한 값을 priority queue에 다시 집어넣어줌.
        heapq.heappush(p_queue, min_1+min_2)