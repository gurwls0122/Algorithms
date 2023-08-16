#https://www.acmicpc.net/problem/13398
import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
# 제거하지 않은 연속합을 저장하기 위한 배열
dp = []

# 한개의 값이 제거된 연속합을 저장하기 위한 배열
dp2= []

for i in range(n):
    if i==0:
        dp.append(lst[i])
        dp2.append(lst[i])
    elif i==1:
        dp.append(max(lst[i], dp[i-1] + lst[i]))
        dp2.append(max(dp[i-1], lst[i]))
    else:
        dp.append(max(lst[i], dp[i-1]+ lst[i]))
        dp2.append(max(dp2[i-1]+lst[i], dp[i-1]))

print(max(max(dp), max(dp2)))