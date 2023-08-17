#https://www.acmicpc.net/problem/3190
import sys
from collections import deque
#보드의 크기
N = int(sys.stdin.readline())
#사과의 갯수
K = int(sys.stdin.readline())
#사과 위치
apple =[list(map(int , sys.stdin.readline().split())) for _ in range(K)]

#뱀의 방향전환 횟수
L = int(sys.stdin.readline())
#뱀의 방향전환 정보
snake = deque([list(map(str, sys.stdin.readline().split())) for _ in range(L)])

# 뱀의 위치를 저장하기 위한 변수 y, x
y, x = 0, 0

# 뱀이 움직일 방향을 정할 변수
# 오른쪽으로 돌시 idx +1, 왼쪽으로 돌시 idx-1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 방향을 기억하고 있을 변수
dirc = 0

#뱀의 위치 정보를 모두 가지고 있는 queue
queue = deque([(y, x)])

# 시간 순서대로 한칸씩 이동
# 보드 크기만큼 움직일 수 있으므로 반복은 N^2
for i in range(1, N**2+1):   
    # print(i)
    #1. 움직인 위치에 머리가 박는지 안박는지 확인
    y = y + dy[dirc]
    x = x + dx[dirc]

    if y<0 or y>=N or x<0 or x>=N or (y, x) in queue:
        print(i)
        break
    
    #2. 머리를 안박았다면 새로 움직일 위치 queue에 추가
    queue.append((y, x))

    #3. 움직인 위치에 사과가 있는지 확인하고 있다면 꼬리를 유지, 없다면 꼬리 자르기
    flag = False
    for j in range(len(apple)):
        if apple[j] == [y+1, x+1]:
            flag = True
            del apple[j]
            break
    if not flag: 
        queue.popleft()
        
    #4. 방향을 보고 바꾸기
    if len(snake) !=0 and i == int(snake[0][0]):
        if snake[0][1] == "L":
            dirc = (dirc-1)%4
        else:
            dirc = (dirc+1)%4

        snake.popleft()
    
    # print(queue)
    # print(dirc)
    # print(apple)