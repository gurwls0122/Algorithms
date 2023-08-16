#https://www.acmicpc.net/problem/2493
# import sys
# N = int(sys.stdin.readline())
# top = list(map(int, sys.stdin.readline().split()))

# ans = [0]
# max_height = top[0]
# for i in range(1, N):
#     if top[i] > top[i-1]:
#         if max_height < top[i]:
#             ans.append(0)
#             max_height = top[i]
#         else:
#             ans.append(ans[i-1])
#     else:
#         ans.append(i)
# print(*ans)

import sys
N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))

ans = [0]
stack = [(top[0], 1)]
for i in range(1, N):
    while stack:
        if stack[-1][0] < top[i]:
            stack.pop()
        else:
            ans.append(stack[-1][1])
            stack.append((top[i], i+1))
            break
    if stack ==[]:
        ans.append(0)
        stack.append((top[i], i+1))
    
print(*ans)