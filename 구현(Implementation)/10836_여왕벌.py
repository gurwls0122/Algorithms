#https://www.acmicpc.net/problem/10836

import sys
M, N = map(int, sys.stdin.readline().split())
worm = [1] * (2*M - 1)
for _ in range(N):
    plus_0, plus_1, plus_2 = map(int, sys.stdin.readline().split())
    tmp = plus_0
    for i in range(tmp, tmp+plus_1):
        worm[i] += 1
    for i in range(tmp+plus_1, 2*M-1):
        worm[i] += 2
    
board = [([1] * M) for _ in range(M)]

for i in range(M):
    for j in range(M):
        if i==0:
            board[i][j] = worm[M-1+j]
        elif j==0:
            board[i][j] = worm[M-1-i]
        else:   
            board[i][j] = board[i-1][j]

for i in range(M):
    print(*board[i])
