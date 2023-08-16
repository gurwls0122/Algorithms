#https://www.acmicpc.net/problem/1174
import sys
N = int(sys.stdin.readline())
ans = set()

def backtracking(num):
    if len(str(num)) == 1:
        ans.add(num)
    for i in range(10):
        if int(str(num)[-1]) > i:
            ans.add(int(str(num) + str(i)))
            backtracking(int(str(num) + str(i)))
        else:
            continue        

if __name__ == "__main__":
    for i in range(10):
        backtracking(i)
    ans = sorted(list(ans))
    if len(ans) >= N:
        print(ans[N-1])
    else:
        print(-1)