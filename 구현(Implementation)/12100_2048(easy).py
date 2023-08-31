#https://www.acmicpc.net/problem/12100
import sys
import copy
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_val = 0

#direction은 방향을 나타냄. 상하좌우 순으로 0, 1, 2, 3
def backtraking(new_board, direction):
    if direction ==0:
        # print("여기 들어옴")
        # i는 x축을 탐색함
        for i in range(N):
            queue = []
            for j in range(N):
                if new_board[j][i] != 0:
                    if not queue:
                        queue.append([new_board[j][i], 0])
                    else:
                        if queue[-1][0] == new_board[j][i] and queue[-1][1] == 0:
                            queue[-1]= [new_board[j][i]*2, 1]
                        else:
                            queue.append([new_board[j][i], 0])
            length = len(queue)-1
            # print(queue)
            for k in range(N):
                if k <=length:
                    new_board[k][i] = queue[k][0]
                else:
                    new_board[k][i] = 0
    elif direction == 1:
        #i는 x축을 탐색함
        for i in range(N):
            queue = []
            for j in range(N-1, -1, -1):
                if new_board[j][i] != 0:
                    if not queue:
                        queue.append([new_board[j][i], 0])
                    else:
                        if queue[-1][0] == new_board[j][i] and queue[-1][1] == 0:
                            queue[-1]= [new_board[j][i]*2, 1]
                        else:
                            queue.append([new_board[j][i], 0])
            length = len(queue)-1
            # print(queue)
            idx = 0
            for k in range(N-1, -1, -1):
                if idx <=length:
                    # print(idx)
                    new_board[k][i] = queue[idx][0]
                    idx+=1
                else:
                    new_board[k][i] = 0

    elif direction == 2:
        #i는 y축을 탐색함
        for i in range(N):
            queue = []
            for j in range(N):
                if new_board[i][j] != 0:
                    if not queue:
                        queue.append([new_board[i][j], 0])
                    else:
                        if queue[-1][0] == new_board[i][j] and queue[-1][1] == 0:
                            queue[-1]= [new_board[i][j]*2, 1]
                        else:
                            queue.append([new_board[i][j], 0])
            length = len(queue)-1
            # print(queue)
            for k in range(N):
                if k <=length:
                    new_board[i][k] = queue[k][0]
                else:
                    new_board[i][k] = 0        
    else: #direction이 3
        for i in range(N):
            queue = []
            for j in range(N-1, -1, -1):
                if new_board[i][j] != 0:
                    if not queue:
                        queue.append([new_board[i][j], 0])
                    else:
                        if queue[-1][0] == new_board[i][j] and queue[-1][1] == 0:
                            queue[-1]= [new_board[i][j]*2, 1]
                        else:
                            queue.append([new_board[i][j], 0])
            length = len(queue)-1
            # print(queue)
            idx = 0
            for k in range(N-1, -1, -1):
                if idx <=length:
                    new_board[i][k] = queue[idx][0]
                    idx+=1
                else:
                    new_board[i][k] = 0 
    # print("=========================")
    # print(direction)
    # print(new_board)
    # print("======================")
    
    return new_board

def dfs(board, cnt):
    global max_val
    if cnt==5:
        for i in range(N):
            max_val = max(max_val, max(board[i]))
        return
    
    for i in range(4):
        new_board = backtraking(copy.deepcopy(board), i)
        dfs(new_board, cnt+1)

if __name__ =="__main__":
    dfs(board, 0)
    print(max_val)