#https://www.acmicpc.net/problem/2467
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

#두 용액의 농도를 저장할 리스트
ans = []

#두 용액의 농도 합을 저장할 변수
#최대값이 20억이므로 이보다 큰 수를 저장
density = 2 * 10e9 + 1

#포인터를 두개 두고 양쪽에서 한칸씩 전진하며 계산
start = 0
end = len(lst)-1

#두개의 포인터가 겹치지 않을때까지 반복
while start<end:
    #저장되어있는 농도의 절대값이 현재 계산한 절대값보다 크다면
    if abs(tmp:=lst[start] + lst[end]) <=abs(density):
        #기존에 저장되어 있는 답을 pop해주고
        if len(ans):
            ans.pop()
        #새로운 답을 저장해준다
        ans=[lst[start], lst[end]]
        #+농도도
        density = tmp

    #이번 반복때 계산한 농도값이 0이라면 반복 종료
    if tmp == 0:
        break
    #양수일 경우 오른쪽 포인터를 왼쪽으로 한칸 옮김
    elif tmp >0:
        end -=1
    #음수일 경우 왼쪽 포인터를 오른쪽으로 한칸 옮김
    else:
        start+=1

print(*ans)