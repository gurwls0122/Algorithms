import sys
V, E = map(int, sys.stdin.readline().split())
#graph에는 순서대로 A번 정점, B번 정점, 가중치가 튜플로 묶여 리스트에 저장된다.
graph = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
parent = [i for i in range(V+1)]

def union(a, b):
    node_a = find(a)
    node_b = find(b)

    if node_a>node_b:
        parent[node_a] = node_b
    else:
        parent[node_b] = node_a


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

if __name__=="__main__":
    ans = 0
    graph.sort(key= lambda x: x[2])
    # print(graph)
    for line in graph:
        a, b, cost = line
        # 부모가 같을때 -> cycle이 생길 때
        if find(a) == find(b):
            continue
        else:
            union(a, b)
            # print(a, b)
            # print(parent)
            ans+=cost
print(ans)