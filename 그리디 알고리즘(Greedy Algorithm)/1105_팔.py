#https://www.acmicpc.net/problem/1105
import sys
L, R = map(str, sys.stdin.readline().split())

ans = 0
if len(L) != len(R):
    pass
else:
    for i in range(len(L)):
        if int(L[i]) == int(R[i]):
            if int(L[i]) == 8:
                ans+=1
            else:
                pass
        else:
            break

print(ans)