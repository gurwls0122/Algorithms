#https://www.acmicpc.net/problem/1107
# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
# ans = 0

# if M == 0:
#     lst = []
# else:
#     lst = list(map(int, sys.stdin.readline().split()))

# #1. 큰 자리수 부터 탐색하여 채널과 다른값이 나올 때까지 탐색
# #다른값이 나온다면 해당 값을 기준으로 원래 채널과 가장 가까운 숫자를 만듬

# #채널을 탐색하기위해 str으로 만든 변수
# str_N = str(N)

# #채널과 가장 유사한 숫자를 저장해놓을 변수
# alike_num = ""

# #채널보다 값이 큰지, 값이 작은지, 값이 같은지 판단할 변수
# # 0 : 현재까지 채널과 값이 동일
# # 1 : 값이 채널보다 큼
# # 2 : 값이 채널보다 작음
# channel_check = 0

# for i in range(len(str_N)):
#     if channel_check == 0:
#         if int(str_N[i]) not in lst:
#             alike_num+=str_N[i]
#         else:

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ans = abs(N-100)

if M == 0:
    lst = []
else:
    lst = list(map(int, sys.stdin.readline().split()))

for num in range(1000001):
    num = str(num)
    for idx in range(len(num)):
        if int(num[idx]) in lst:
            break
        elif idx == len(num)-1:
            ans = min(ans, len(str(num)) + abs(int(num)-N))

print(ans)