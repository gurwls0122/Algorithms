#https://www.acmicpc.net/problem/1644
import sys
N = int(sys.stdin.readline())

#step 1: 1부터 N까지의 정수중에서 소수 모두 구하기
#sieve : 에라토스테네스의 체를 구하기 위한 각 숫자별 소수 여부
#prime_lst : 소수만 모아둔 리스트
sieve = [False, False] + [True] * (N-1)
prime_lst = []

for i in range(2, N+1):
    if sieve[i]:
        prime_lst.append(i)
        for j in range(2*i, N+1, i):
            sieve[j] = False

#step 2: 포인터 두개를 유지하며 연속된 소수가 해당 값을 출력할 수 있는지 확인
#ans : 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 저장할 변수
ans = 0
#start, end : 투포인터의 시작과 끝
start, end = 0, 1
#start부터 end까지의 값을 저장해놓을 변수 val
val = 0

#포인터가 범위를 넘어가면 종료!
while start<=len(prime_lst) and end<=len(prime_lst):
    val = sum(prime_lst[start:end])

    #만약, 연속된 소수가 N보다 작은데 end 포인터가 끝이라면(값이 더 커질 수 없다면) 종료
    if val < N and end == len(prime_lst):
        break

    #일반 경우
    #1. 범위의 값이 N보다 크면, start를 1만큼 올림(값을 줄임)
    if val > N:
        start +=1
    #2. 범위의 값이 N보다 작으면, end를 1만큼 올림(값을 올림)
    elif val < N:
        end +=1
    #3. 범위의 값이 N과 같다면, 답을 1만큼 올려주고
    #값을 더 키울수 있다면 키우고 아니면 종료
    else:
        ans+=1
        if end < len(prime_lst):
            end+=1
        else:
            break

print(ans)