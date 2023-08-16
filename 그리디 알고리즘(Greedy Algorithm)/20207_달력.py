#https://www.acmicpc.net/problem/20207
import sys
N = int(sys.stdin.readline())
calendar = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

coating = [0] * 365

for start, end in calendar:
    for i in range(start-1, end):
        coating[i] +=1

ans = 0
garo, sero = 0, 0
for i in coating:
    if i==0:
        ans += garo*sero
        sero = 0
        garo = 0
    else:
        garo +=1
        sero = max(sero, i)

ans += garo * sero
print(ans)