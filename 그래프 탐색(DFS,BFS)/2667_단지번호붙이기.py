import sys
from collections import deque
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(board, N):
    visited =[[0] * N for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and visited[i][j] == 0:
                count = 0 
                queue = deque([(i, j)])
                while queue:
                    row, col = queue.popleft()
                    if visited[row][col] ==0:
                        count +=1
                        visited[row][col] = 1
                        for k in range(4):
                            if 0<=row+dy[k] <= N-1 and 0<=col + dx[k]<=N-1 and board[row+dy[k]][col+dx[k]] == 1:
                                queue.append((row+dy[k], col+dx[k]))
                ans.append(count)
            else:
                continue
    
    return ans

if __name__ =="__main__":
    ans_lst = sorted(bfs(board, N))
    print(len(ans_lst))
    for i in ans_lst:
        print(i)