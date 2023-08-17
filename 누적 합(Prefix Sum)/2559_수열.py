#https://www.acmicpc.net/problem/2559
import sys
N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
max_temp = -10e9

temp = [0]
for i in range(1,N+1):
    temp.append(temp[i-1] + lst[i-1])

for i in range(K, N+1):
    max_temp = max(max_temp, temp[i]-temp[i-K])

print(max_temp)

