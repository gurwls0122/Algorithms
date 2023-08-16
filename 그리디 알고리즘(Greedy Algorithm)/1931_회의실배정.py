#https://www.acmicpc.net/problem/1931
import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

lst.sort(key = lambda x: (int(x[0]), int(x[1])))

ans = []
for i in range(N):
    if i==0:
        ans.append(lst[i])
    else:
        if ans[-1][1] <= lst[i][0]:       #이전 index의 회의가 끝나는시간이 새로운 index의 회의가 시작하는 시간보다 같거나 늦는경우
            ans.append(lst[i])
        else:
            if ans[-1][1] >= lst[i][1]:    #이전 index의 회의가 끝나는 시간이 새로운 index의 회의가 시작하는 시간보다 늦거나 같은경우
                ans.pop()
                ans.append(lst[i])
            else:
                continue
print(len(ans))
