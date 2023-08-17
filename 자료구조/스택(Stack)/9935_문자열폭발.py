#https://www.acmicpc.net/problem/9935
import sys
input_str = sys.stdin.readline().strip()
explos_str = list(map(str,sys.stdin.readline().strip()))

len_explos = len(explos_str)
stack = []

for i in range(len(input_str)):
    stack.append(input_str[i])
    if len(stack)>=len_explos and stack[len(stack)-len_explos:] == explos_str:
        # print(stack[-1-len_explos:-1])
        # print(input_str[i])
        for _ in range(len_explos):
            stack.pop()

if stack == []:
    print("FRULA")
else:
    print(("").join(stack))