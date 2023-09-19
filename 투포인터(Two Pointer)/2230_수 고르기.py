#https://www.acmicpc.net/problem/2230
import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
lst = sorted([int(sys.stdin.readline()) for _ in range(N)])

#값을 비교하기 위해 포인터를 두개 선언(처음과 그 다음)
left, right = 0, 1

#나올 수 있는 최대값이 20억이므로
ans = 2*10e9

#만약, left가 right 범위를 침범하거나 right가 더이상 오른쪽으로 갈 수 없을 때
while left<=right and right<=N-1:
    #포인터 위치에 저장되어 있는 값의 차를 구한후
    tmp = lst[right]-lst[left] 
    #해당 값이 M보다 크다면 ans최신화, 왼쪽 포인터를 옮겨줌
    if tmp >=M:
        ans = min(ans, tmp)
        left+=1
    #해당 값이 M보다 작다면, 값을 더 키워줘야 하므로 오른쪽 포인터를 옮겨줌.
    else:
        right+=1

print(ans)