#https://www.acmicpc.net/problem/17298
import sys
from collections import deque
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

#오큰수를 찾지 못한 값들을 넣어 놓을 스택선언
stack = []

#ans_lst에는 오큰수를 찾았다면 해당 index에 오큰수를 저장
ans_lst = [-1] * N

#index를 0부터 N까지 반복하며
for i in range(N):
    #스택에 (val, idx)형태로 값을 저장하고
    if i==0:
        stack.append((lst[i], i))
    else:
        #stack의 오른쪽부터 확인을 하며 자신보다 작은 값이 있으면 계속해서 pop해나가고
        while stack:
            if stack[-1][0] < lst[i]:
                val, idx = stack.pop()
                ans_lst[idx] = lst[i]
            #자신보다 큰 값이 있는 경우 바로 break(이미 왼쪽에서 내림차순으로 정렬되어 있을 것이므로)
            else:
                break
        
        stack.append((lst[i], i))

print(*ans_lst)