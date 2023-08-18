#https://www.acmicpc.net/problem/5557
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

#dp배열에는 해당 index에서 가질 수 있는 값과 그 값이 나올 수 있는 갯수가 튜플로 주어진다.

dp = [[] for _ in range(N-1)]

for i in range(N-1):
    if i==0:
        dp[i].append([lst[i], 1])
    else:
        # print(lst[i])
        for val, cnt in dp[i-1]:
            # print(val, cnt)
            if val+lst[i]>20:
                pass
            else:
                if len(dp[i])==0:
                    dp[i].append([val+lst[i], cnt])
                else:
                    for k in range(len(dp[i])):
                        if dp[i][k][0] == val+lst[i]:
                            dp[i][k][1] += cnt
                            break
                        if k== len(dp[i])-1:
                            dp[i].append([val+lst[i], cnt])
            if val-lst[i]<0:
                pass
            else:
                if len(dp[i])==0:
                    dp[i].append([val-lst[i], cnt])
                else:
                    for k in range(len(dp[i])):
                        if dp[i][k][0] == val-lst[i]:
                            dp[i][k][1] += cnt
                            break
                        if k == len(dp[i])-1:
                            dp[i].append([val-lst[i], cnt])
for i in range(len(dp[-1])):
    if dp[-1][i][0] == lst[-1]:
        print(dp[-1][i][1])
        exit()

print(0)
