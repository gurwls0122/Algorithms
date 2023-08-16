#https://www.acmicpc.net/problem/5014
import sys
#총 층수 F, 현재 위치 S, 스타트링크 위치 G, 위로 U층, 아래로 D층
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [False] * (F+1)

def bfs():
    queue = deque([(S, 0)])
    visited[S] = True
    while queue:
        cur_loc, depth = queue.popleft()
        visited[cur_loc] = True
        # print(cur_loc, depth)
        if cur_loc == G:
            print(depth)
            exit(0)
        else:
            #BFS는 queue에 넣는 순간에 방문 체크를 해야 중복 방문이 일어나지 않음..!
            if cur_loc + U <=F and not visited[cur_loc+U]:
                # visited[cur_loc+U] = True
                queue.append((cur_loc+U, depth+1))
            
            if cur_loc - D >0 and not visited[cur_loc-D]:
                # visited[cur_loc-D] = True
                queue.append((cur_loc-D, depth+1))
    print("use the stairs")
    return

if __name__ == "__main__":
    bfs()