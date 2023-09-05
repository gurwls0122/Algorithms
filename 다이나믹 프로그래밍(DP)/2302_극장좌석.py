#https://www.acmicpc.net/problem/2302
import sys
N = int(sys.stdin.readline())

#VIP가 아닌 좌석은 0으로 초기화
seat = [0 for _ in range(N)]
M = int(sys.stdin.readline())
#VIP인 좌석은 1로 설정
for _ in range(M):
    vip = int(sys.stdin.readline())
    seat[vip-1] = 1

#정답을 저장할 변수
ans = 1
#피보나치 배열을 선언해서 피보나치 수열을 좌석의 갯수만큼 반복
fib = [1, 1]
for i in range(2, N+1):
    fib.append(fib[i-1] + fib[i-2])

#VIP좌석은 고정되어 있으므로 VIP좌석을 기준으로 boundary를 나눔
#해당 boundary에 몇개의 좌석이 있는지 확인하기 위한 cnt함수
cnt = 0

#VIP좌석이 아니라면 cnt+1
for i in range(N):
    if seat[i] == 0:
        cnt+=1
    #VIP좌석이라면 현재까지 세었던 cnt에 해당하는 피보나치 수를 정답에 곱해줌.
    else:
        ans *= fib[cnt]
        cnt = 0      
#VIP좌석이 나오지 않고 종료되었을 수도 있으므로 답을 출력하기전에 한번더 계산해줌.
ans*=fib[cnt]

print(ans)