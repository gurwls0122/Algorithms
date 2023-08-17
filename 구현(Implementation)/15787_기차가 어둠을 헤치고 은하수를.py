#https://www.acmicpc.net/problem/15787
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
train = [deque([0] * 20) for _ in range(N)]

for _ in range(M):
    inp = list(map(int, sys.stdin.readline().split()))
    #1 i x : i번째 기차 x번째 좌석에 사람을 태워라. 이미 사람이 타있다면 아무런 행동하지 x
    #2 i x : i번째 기차 x번째 앉은 사람을 하차시켜라. 아무도 없다면 아무런 행동하지 x
    #3 i : i번째 기차에 앉은 모든 승객들이 한칸씩 뒤로 간다. 20번째 앉은 사람은 하차
    #4 i : i번째 기차에 앉은 모든 승객들이 앞으로 온다. 1번째 앉은 사람은 하차
    if inp[0] == 1:
        train[inp[1]-1][inp[2]-1] = 1
    elif inp[0] == 2:
        train[inp[1]-1][inp[2]-1] = 0
    elif inp[0] == 3:
        train[inp[1]-1].pop()
        train[inp[1]-1].appendleft(0)
    else:   #inp[0] == 4
        train[inp[1]-1].append(0)
        train[inp[1]-1].popleft()

# print(train)
ans_lst = []
for i in range(N):
    if train[i] not in ans_lst:
        ans_lst.append(train[i])
        
print(len(ans_lst))