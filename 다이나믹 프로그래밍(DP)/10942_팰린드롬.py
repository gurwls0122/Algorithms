##https://www.acmicpc.net/problem/10942
import sys
N = int(sys.stdin.readline())
#입력받은 숫자 배열
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

#board[i][j] : i번째에서 시작해서 j번째까지 숫자 배열이 팰린드롬인지 확인
# -1일때 : i보다 j가 커서 들르지않음 / 0일때 : 팰린드롬이 아님 / 1일때 : 팰린드롬임
board = [[-1] * N for _ in range(N)]

#열을 나중에 돌도록 함
for j in range(N):
    #행을 먼저 돌아야 됨. why? 계산하는 과정에서 더 높은 행을 확인해야되는 경우가 생김
    for i in range(N):
        #i -> j가 성립자체가 안될 경우
        if i>j:
            pass
        #i-> j가 같으면 팰린드롬
        elif i==j:
            board[i][j] = 1
        #i -> j가 정상적일 경우
        else:
            #1. 시작지점 +1 부터 끝지점 -1까지가 팰린드롬이고 시작지점, 끝지점 값이 같거나
            #2. 시작지점 +1 부터 끝지점 -1까지가 성립이 안되고(-1이고), 끝지점이 값이 같다면
            if (board[i+1][j-1] == 1 or board[i+1][j-1]==-1) and lst[i]== lst[j]:
                #팰린드롬
                board[i][j] = 1
            #아니면
            else:
                #팰린드롬 아님ㅋ
                board[i][j] = 0

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(board[start-1][end-1])
