#https://www.acmicpc.net/problem/1987
import sys
R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
#각 알파벳별 방문여부를 저장해놓을 리스트
ans_lst = [0] * 26
max_cnt = 0

#상하좌우 탐색할 변수
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def backtracking(row, col, cnt):
    #max_cnt는 글로벌로 선언
    global max_cnt
    
    #현재 자신의 위치를 숫자로 기억하기 위해 ord 사용
    node_num = ord(board[row][col])-65
    
    #만약, 현재 자신의 위치에 있는 알파벳이 이미 방문처리되어있다면, 최대 거리를 update해주고 종료
    if ans_lst[node_num]:
        max_cnt = max(max_cnt, cnt)
        return 
    #현재 자신의 위치에 있는 알파벳을 방문하지 않았다면,
    else:
        #방문처리 해주고
        ans_lst[node_num] +=1
        #현재까지 방문한 알파벳 숫자를 1만큼 더해주고
        cnt+=1

        #상하좌우 4방향을 확인하면서
        for i in range(4):
            #움직일 수 있다면 해당 위치에서 재귀 호출
            if 0<=row+dy[i] <R and 0<=col+dx[i]<C:
                backtracking(row+dy[i], col+dx[i], cnt)
            else:
                continue
        #재귀 호출 종료 시, 원상 복구 해줘야 됨.
        ans_lst[node_num]-=1
        cnt-=1

if __name__ == "__main__":
    backtracking(0, 0, 0)
    print(max_cnt)