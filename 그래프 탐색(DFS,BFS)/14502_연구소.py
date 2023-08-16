# https://www.acmicpc.net/problem/14502
#1.연구소에서 벽 or 바이러스가 존재하지 않는 방을 찾는다(0인곳)
#2.해당 방중 3개를 선택하여 벽을 세운후 바이러스가 어디까지 퍼지는지 확인한다.
#3.전체 탐색을 진행하며 안전구역이 가장 넓을 때를 찾는다(N, M이 최대가 8이고 벽을 세개만 고를 것이므로 시간초과 나지 않음)

import sys
import copy
from collections import deque
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0

def bfs(new_board):
    #lst에는 바이러스에 전염된 곳의 좌표가 들어감
    lst = deque([])
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 2:
                lst.append((i, j))

    #전염된 곳을 돌아가며 주위 확인
    while lst:
        y, x = lst.popleft()
        for k in range(4):
            if (0<= y+dy[k] <N and 0<= x+dx[k] <M) and new_board[y+dy[k]][x+dx[k]]==0:
                new_board[y+dy[k]][x+dx[k]] = 2
                lst.append((y+dy[k], x+dx[k]))
    count = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                count+=1
    return count

#지도중 0을 가지고 있는 좌표를 저장해 놓을 수 있는 리스트
lst = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            lst.append((i, j))

for a1, a2, a3 in combinations(lst, 3):
    new_board = copy.deepcopy(board)
    new_board[a1[0]][a1[1]] = 1
    new_board[a2[0]][a2[1]] = 1
    new_board[a3[0]][a3[1]] = 1
    ans = max(bfs(new_board), ans)

print(ans)



