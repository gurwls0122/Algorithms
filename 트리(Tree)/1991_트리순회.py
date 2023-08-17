import sys
from collections import deque
N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().strip().split())
    tree[root] = (left, right)

def preorder(root):
    queue = deque([root])
    while queue:
        root_node = queue.popleft()
        if root_node == ".":
            continue
        else:
            print(root_node, end="")
            queue.appendleft(tree[root_node][1])
            queue.appendleft(tree[root_node][0])
    print()

def inorder(root):
    if tree[root][0] != ".":
        inorder(tree[root][0])
    print(root, end="")
    if tree[root][1] != ".":
        inorder(tree[root][1])

def postorder(root):
    if tree[root][0] !=".":
        postorder(tree[root][0])
    if tree[root][1] != ".":
        postorder(tree[root][1])
    print(root, end="")


if __name__ =="__main__":
    preorder('A') 
    inorder('A')
    print()
    postorder('A')
    print()