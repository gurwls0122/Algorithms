#https://www.acmicpc.net/problem/1647
import sys
N, M = map(int, sys.stdin.readline().split())
#입력받은 길의 정보들을 길의 유지비 순서대로 정렬하여 저장
road = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(M)], key=lambda x: x[2])
#union-find를 진행할때 자신의 부모 노드를 저장해두기 위한 배열
parent = [i for i in range(N+1)]

def find(x):
    #만약 자신의 부모가 자신이 아니라면(root노드가 아니라면) root노드가 나올때까지 찾음
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    #각 노드의 root노드를 찾아서
    root_a = find(a)
    root_b = find(b)

    #더 작은값이 root노드에 올라갈 수 있도록 변경
    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a

if __name__ =="__main__":
    ans_lst = []
    for a, b, cost in road:
        if find(a) != find(b):
            ans_lst.append(cost)
            union(a, b)
        else:
            continue
    #마을을 두개로 나눈다는 것은 MST를 구하고 그중에서 가장 큰 길의 값을 제외하면 된다는 것이니..
    print(sum(ans_lst[:-1]))