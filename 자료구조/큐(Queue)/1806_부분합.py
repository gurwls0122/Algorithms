#https://www.acmicpc.net/problem/1806
import sys
from collections import deque
N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
#ans : 부분합 길이의 최대값이 10만이므로 이보다 큰 수로 초기화
#tmp : 현재 저장되어있는 부분합의 값을 나타내는 정보
#len_lst : 현재 저장되어있는 부분합의 길이를 나타내는 정보
ans, tmp, len_lst = 10e5+1, 0, 0

#queue로 초기화해서 값이 S이상이 되면 S보다 작을때까지 빼는 로직을 진행할 예정
ans_lst = deque([])

#lst를 모두 탐방해도 마지막 값에 대한 부분합 정보를 대입해줘야 하므로 반복을 N+1번 진행
for i in range(N+1):
    # 만약, 현재까지 부분합이 S이상이라고 하면
    if tmp >= S:
        #부분합 값중에 작은 값을 답으로 취하고
        ans = min(ans, len_lst)
        #부분합 값이 S보다 작아질때까지 부분합을 빼줌(queue에서 제외)
        while tmp >S:
            ans = min(ans, len_lst)
            tmp -= ans_lst.popleft()
            len_lst-=1
    else:
        pass
    #마지막 반복에서는 추가하는 logic을 뺴줘야하므로
    if i<N:
        tmp += lst[i]
        ans_lst.append(lst[i])
        len_lst+=1

if tmp >= S:
    ans = min(ans, len_lst)

if ans == 10e5+1:
    print(0)
else:
    print(ans)
