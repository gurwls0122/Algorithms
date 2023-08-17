#https://www.acmicpc.net/problem/11660
import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        board[i][j] += board[i][j-1]

for j in range(N):
    for i in range(1, N):
        board[i][j] += board[i-1][j]

# print(board)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 ==1 and y1 == 1:
        print(board[x2-1][y2-1])
    elif x1 ==1:
        print(board[x2-1][y2-1] - board[x2-1][y1-2])
    elif y1 ==1:
        print(board[x2-1][y2-1] - board[x1-2][y2-1])
    else:
        print(board[x2-1][y2-1] - board[x2-1][y1-2] - board[x1-2][y2-1] + board[x1-2][y1-2])