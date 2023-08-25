#https://www.acmicpc.net/problem/14621
import sys
N, M = map(int, sys.stdin.readline().split())
#각 학교가 남초인지 여초인지 확인하기 위한 판단 기준이 되는 list
judge = list(map(str, sys.stdin.readline().split()))

#입력받은 경로를 저장해놓는 리스트
path = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(M)], key=lambda x : x[2])

#Union-Find를 진행하기 위해 자신의 부모 노드를 저장해놓는 리스트
parent = [i for i in range(N+1)]

#find함수. 각 노드의 부모는 계속 갱신됨.
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

#union함수. 작은 노드 값이 부모로 갈 수 있도록 설계
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a
    
if __name__ == "__main__":
    #답을 저장해놓을 변수
    ans = 0
    for a, b, cost in path:
        #만약, 대학교가 동일한 성별의 대학교라면 실행하지 x
        if judge[a-1] != judge[b-1]:
            #사이클이 생기지 않을때만 union & cost 저장
            if find(a) != find(b):
                union(a,b)
                ans+=cost
            else:
                continue
        else:
            continue

    for i in range(1, N+1):
        find(i)

    if len(set(parent[1:])) == 1:
        print(ans)
    else:
        print(-1)