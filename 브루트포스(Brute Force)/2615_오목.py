#https://www.acmicpc.net/problem/2615
import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]
for i in range(19):
    for j in range(19):
        if board[i][j] !=0:
            flag = board[i][j]
            for idx in range(4):
                x = j + dx[idx]
                y = i + dy[idx]
                count = 1
                
                while 0<=x<19 and 0<=y<19 and board[y][x] == flag:
                    count+=1

                    if count==5:
                        if 0<=j - dx[idx] <19 and 0<= i - dy[idx]<19 and board[i-dy[idx]][j-dx[idx]]==flag:
                            break
                        if 0<=x + dx[idx]<19 and 0<=y + dy[idx]<19 and board[y+dy[idx]][x+dx[idx]] == flag:
                            break
                        print(flag)
                        print(i+1, j+1)
                        exit()
                    x+=dx[idx]
                    y+=dy[idx]
        else:
            continue
print(0)