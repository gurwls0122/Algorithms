#https://www.acmicpc.net/problem/2096
import sys
N = int(sys.stdin.readline())
#최대값, 최소값을 저장하기 위한 변수
#9가 100,000나올때 가장 큰 값이 나오기때문에 10e6으로 초기화.
max_ans = 0
min_ans = 10e6

for i in range(N):
    #입력값을 left, center, right에 저장
    left, center, right = map(int, sys.stdin.readline().split())
    #dp배열은 각각 [가질수 있는 최소값, 가질수 있는 최대값]으로 선언 되며
    #i==0일때는 자기자신값이 최소, 최대값임
    if i==0:
        dp = [[left, left],[center, center], [right, right]]
    else:
        #i==0이 아닐때는 자신의 값 + 자신보다 하나 높은 index에서의 최소값, 최대값을 이용해서 구해줌
        #tmp를 안 쓰고 dp로 바꾼다면 계산되기전에 덮어씌워지므로 주의!
        tmp0 = [left + min(dp[0][0], dp[1][0]), left + max(dp[0][1], dp[1][1])]
        tmp1 = [center + min(dp[0][0], dp[1][0], dp[2][0]), center + max(dp[0][1], dp[1][1], dp[2][1])]
        tmp2 = [right + min(dp[1][0], dp[2][0]), right + max(dp[1][1], dp[2][1])]

        dp[0] = tmp0
        dp[1] = tmp1
        dp[2] = tmp2

    # print(dp)
    # 마지막 반복일때, 최대/최소 값 구해주기
    if i==N-1:
        for j in dp:
            max_ans = max(j[1], max_ans)
            min_ans = min(j[0], min_ans)

print(max_ans, min_ans)