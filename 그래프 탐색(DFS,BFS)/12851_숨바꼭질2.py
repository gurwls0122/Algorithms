#https://www.acmicpc.net/problem/12851
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [False] * (max(N,K)*2+1)
time = 10e6
count = 0

def bfs(loc, depth):
    global time, count
    queue = deque([(loc, depth)])

    while queue:
        cur_loc, cur_depth = queue.popleft()
        visited[cur_loc] = True
        # print(cur_loc, cur_depth)
        if cur_loc ==K:
            if time < cur_depth:
                break
            elif time==cur_depth:
                count += 1
            else:
                time = cur_depth
                count = 1
        elif cur_loc > K:
            if not visited[cur_loc-1]:
                queue.append((cur_loc-1, cur_depth+1))
        else:
            # print(cur_loc*2)
            if cur_loc-1 >=0 and not visited[cur_loc-1]:
                queue.append((cur_loc-1, cur_depth+1))
            if not visited[cur_loc+1]:
                queue.append((cur_loc+1, cur_depth+1))
            if not visited[cur_loc*2]:
                queue.append((cur_loc*2, cur_depth+1))


if __name__ == "__main__":
    bfs(N, 0)
    print(time)
    print(count)