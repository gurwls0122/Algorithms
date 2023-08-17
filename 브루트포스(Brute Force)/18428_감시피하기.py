# https://www.acmicpc.net/problem/18428
import sys
import copy
from itertools import combinations
from collections import deque
N = int(sys.stdin.readline())
board = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(new_board):
    # print("=============================")
    is_avoid = True
    #선생님 위치 찾기
    #queue에는 y좌표, x좌표, 확인하고 있는 방향순으로 나타낸다
    #확인하고 있는 방향은 0-> 전체/1-> 오른쪽/2->위/3-> 왼쪽/4->아래
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if new_board[i][j] == "T":
                queue.append((i, j, 0))
    
    while queue:
        y, x, idx = queue.popleft()
        # print(y, x, idx)
        if idx == 0 or idx ==1:
            # print(1)
            if 0<=y+dy[0]<N and 0<=x+dx[0]<N:
                if new_board[y+dy[0]][x+dx[0]] in ["X","T"]:
                    queue.append((y+dy[0], x+dx[0], 1))
                elif new_board[y+dy[0]][x+dx[0]] == "S":
                    is_avoid = False
                    break
                else:#벽을 만났을 경우("F")
                    pass
            else:
                pass
        if idx==0 or idx==2:
            # print(2)
            if 0<=y+dy[1]<N and 0<=x+dx[1]<N:
                if new_board[y+dy[1]][x+dx[1]] in ["X","T"]:
                    queue.append((y+dy[1], x+dx[1], 2))
                elif new_board[y+dy[1]][x+dx[1]] == "S":
                    is_avoid = False
                    break
                else:#벽을 만났을 경우("F")
                    pass
            else:
                pass
        if idx==0 or idx==3:
            # print(3)
            if 0<=y+dy[2]<N and 0<=x+dx[2]<N:
                if new_board[y+dy[2]][x+dx[2]] in ["X","T"]:
                    queue.append((y+dy[2], x+dx[2], 3))
                elif new_board[y+dy[2]][x+dx[2]] == "S":
                    is_avoid = False
                    break
                else:#벽을 만났을 경우("F")
                    pass
            else:
                pass
        if idx==0 or idx==4:
            # print(4)
            if 0<=y+dy[3]<N and 0<=x+dx[3]<N:
                if new_board[y+dy[3]][x+dx[3]] in ["X","T"]:
                    queue.append((y+dy[3], x+dx[3], 4))
                elif new_board[y+dy[3]][x+dx[3]] == "S":
                    is_avoid = False
                    break
                else:#벽을 만났을 경우("F")
                    pass
            else:
                pass
    # if is_avoid == True:
    #     print(new_board)
    return is_avoid 

if __name__ == "__main__":
    # 1. 아무것도 존재하지 않는 위치 X의 좌표를 모두 찾기
    find_X = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == "X":
                find_X.append((i, j))

    # 2. 장애물을 3개만 설치 해야하므로 X의 좌표중에서 3개를 뽑아 감시를 피할 수 없는지 확인
    for cords in combinations(find_X, 3):
        new_board = copy.deepcopy(board)
        for y, x in cords:
            new_board[y][x] = "F"
        
        if bfs(new_board):
            print("YES")
            exit()
    
    print("NO")