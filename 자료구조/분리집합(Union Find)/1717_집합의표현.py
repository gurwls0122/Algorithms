#https://www.acmicpc.net/problem/1717
import sys
n, m = map(int, sys.stdin.readline().split())

#union find를 실행하기 위해 각 index의 부모를 저장해놓을 list 선언
parent = [i for i in range(n+1)]

#find 함수
def find(num):
    #만약, 자신이 root 노드가 아니라면(parent에 저장되어있는 값이 index와 다르다면)
    if parent[num] != num:
        #자신의 부모 노드를 상대로 find함수 재귀적 반복
        parent[num] = find(parent[num])
    #자신이 root 노드라면 return
    return parent[num]

def union(a, b):
    #a와 b의 root노드를 탐색한 후
    a = find(a)
    b = find(b)
    #더 큰 root를 가진 값에 대입
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    tmp, a, b = map(int, sys.stdin.readline().split())
    if tmp==0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")
