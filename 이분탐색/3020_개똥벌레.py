#https://www.acmicpc.net/problem/3020
import sys
N, H = map(int, sys.stdin.readline().split())
down = [0] * (H+1)
up = [0] * (H+1)

for i in range(N):
    if i%2==0:
        down[int(sys.stdin.readline())]+=1
    else:
        up[int(sys.stdin.readline())] +=1

for i in range(H-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_obst, count = N, 0

# print(down)
# print(up)
for i in range(1, H+1):
    obst_count = down[i] + up[H-i+1]
    if min_obst > obst_count:
        min_obst = obst_count
        count = 1
    elif min_obst == obst_count:
        count+=1

print(min_obst, count)