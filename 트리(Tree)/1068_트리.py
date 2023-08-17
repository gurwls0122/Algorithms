#https://www.acmicpc.net/problem/1068
import sys
from collections import defaultdict
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
del_node = int(sys.stdin.readline())

#tree를 딕셔너리 형태로 선언
tree = defaultdict(list)

for i in range(N):
    tree[i] = []

#딕셔너리에 트리형태로 저장. 리프 노드일 경우 자식 개수 0
for i in range(N):
    root = lst[i]
    if root != -1:
        tree[root].append(i)

#del_node에서 파생된 모든 노드 제거
def delete_node(del_node, level):
    if level==0:
        for root in tree:
            for i in range(len(tree[root])):
                if tree[root][i] == del_node:
                    tree[root].pop(i)
                    break

    for i in tree[del_node]:
        delete_node(i, level+1)
    
    del tree[del_node]
    print(tree)

#트리를 입력받았을 시 리프 노드가 몇개인지 세어주는 함수
def count_leaf(tree):
    count = 0
    for i in tree:
        if len(tree[i]) == 0:
            count+=1

    return count

if __name__ == "__main__":
    delete_node(del_node, 0)
    print(count_leaf(tree))