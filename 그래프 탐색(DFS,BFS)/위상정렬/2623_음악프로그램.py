#https://www.acmicpc.net/problem/2623
import sys
from collections import defaultdict
import heapq
N, M = map(int, sys.stdin.readline().split())
#Topology Sort를 사용하기 위해 dictionary와 indgree(차수) 리스트 선언
dic = defaultdict(list)
indegree = [0] * (N+1)

#입력 구문
for _ in range(M):
    lst = list(map(int, sys.stdin.readline().split()))
    #자신 뒤에 연결되어야 하는 노드들 dic에 추가하고 indegree 1만큼 늘려줌.
    for i in range(1, lst[0]):
        dic[lst[i]].append(lst[i+1])
        indegree[lst[i+1]] +=1

if __name__ == "__main__":
    #차수가 없는 숫자를 queue에 집어넣음(차수가 없다 == 선행되는 인자가 없다.)
    queue = []

    #답을 저장할 list
    ans_lst = []

    #queue는 작은 수부터 추가했으므로 sorting되어있는 상태일 것임.
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    #queue에 값이 없어질때까지 계속(indegree가 0인 값이 있을때까지 계속)
    while queue:
        #pop되는 순간 print하며 tmp에 변수를 넣어주고
        tmp = heapq.heappop(queue)
        #정답 리스트에 해당 변수 추가
        ans_lst.append(tmp)

        #dic에 pop된 변수의 뒤로 나오는 변수들을 찾아
        for i in dic[tmp]:
            #차수를 한개씩 낮춰주고
            indegree[i] -=1
            #차수가 0이 되었다면 다시 queue에 heappush
            if indegree[i] == 0:
                heapq.heappush(queue, i)
    
if len(ans_lst) == N:
    for i in ans_lst:
        print(i)
else:
    print(0) 