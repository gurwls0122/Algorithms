#https://www.acmicpc.net/problem/4386
import sys
import math
from collections import defaultdict
import heapq
n = int(sys.stdin.readline())
#입력받은 별들의 번호와 좌표값을 기억하고 있는 list
star_lst = []
for i in range(n):
    a, b = map(float, sys.stdin.readline().split())
    star_lst.append((i+1, a, b))

#입력받은 별들끼리의 모든 거리를 저장할 딕셔너리
star_dict = defaultdict(list)
for i in range(n-1):
    for j in range(i+1, n):
        val = round(math.sqrt((star_lst[i][1]-star_lst[j][1])**2 + (star_lst[i][2]-star_lst[j][2])**2), 3)
        star_dict[star_lst[i][0]].append((val, star_lst[j][0]))
        star_dict[star_lst[j][0]].append((val, star_lst[i][0]))

#각 노드의 방문 여부를 기록할 함수
visited = [False] * (n+1)

def prim_alg(node):
    ans = 0
    visited[node] = True
    candidate = star_dict[node]
    heapq.heapify(candidate)

    while candidate:
        cost, near_node = heapq.heappop(candidate)
        if not visited[near_node]:
            ans+=cost
            visited[near_node] = True
            for i in star_dict[near_node]:
                if not visited[i[1]]:
                    heapq.heappush(candidate, i)
        else:
            continue
    return ans

if __name__=="__main__":
    print(prim_alg(1))
