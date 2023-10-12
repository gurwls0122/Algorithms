#https://www.acmicpc.net/problem/4803
import sys
#case 갯수를 셀 수 있는 변수
case_count = 1

#union-find중 find함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

#union-find중 union함수
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a

while True:
    n, m = map(int, sys.stdin.readline().split())
    #0, 0을 입력받으면 종료
    if n==0 and m==0:
        break
    else:
        #각 case별 노드의 부모 노드를 저장해놓을 리스트
        parent = [i for i in range(n+1)]
        #cycle이 생기는 노드를 저장해 놓을 리스트
        del_lst = []
        
        #간선의 갯수만큼 반복하며
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            root_a = find(parent, a)
            root_b = find(parent, b)

            #만약, 입력 노드 사이에 사이클이 만들어 졌을 경우
            if root_a == root_b:
                #해당 노드들을 cycle이 생긴 노드에 저장해놓는다
                del_lst.append(a)
                del_lst.append(b)
            else:
                #입력 노드에 사이클이 만들어지지 않는다면 union
                union(parent, a, b)

        #cycle이 생기는 노드 중복제거
        del_lst = list(set(del_lst))
        
        #cycle이 생기는 노드의 부모 노드를 넣어줌
        for i in range(len(del_lst)):
            del_lst[i] = find(parent, del_lst[i])
        
        #각 노드들의 부모 최신화
        for i in range(1, n+1):
            parent[i] = find(parent, i)
        
        #parent중 사이클이 생기지 않는 노드들만 냄겨둠
        set_lst = set(map(lambda x: x if x not in del_lst else 0, parent))
        cnt = len(set_lst)-1
        
        #출력 구문
        if cnt == 0:
            print(f"Case {case_count}: No trees.")
        elif cnt == 1:
            print(f"Case {case_count}: There is one tree.")
        else:
            print(f"Case {case_count}: A forest of {cnt} trees.")

        #case갯수 추가
        case_count+=1