#https://www.acmicpc.net/problem/5430
import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = deque(list(sys.stdin.readline().strip()[1:-1].split(",")))
    if arr[0] == "":
        arr = deque([])

    flag = True
    right_direction = True
    for i in range(len(p)):
        if p[i] == "R":
            right_direction = not right_direction
        else:   #p[i] =="D"
            if len(arr) == 0:
                flag =False
                print("error")
                break
            else:
                if right_direction:
                    arr.popleft()
                else:
                    arr.pop()

    if flag:
        if right_direction:
            print("["+",".join(list(arr))+"]")
        else:
            print("["+",".join(list(arr)[::-1])+"]")
