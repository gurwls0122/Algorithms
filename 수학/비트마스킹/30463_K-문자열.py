#https://www.acmicpc.net/problem/30463
import sys
N, K = map(int, sys.stdin.readline().split())

#0부터 9까지의 숫자가 있고 없고를 2진수로 나타냄. 2^10-1만큼의 갯수가 필요 => 1024개 필요
lst = [0] * 1024

#1. 입력 받은 숫자를 이진수로 변환. 
for _ in range(N):
    tmp = ['0'] * 10
    in_str = sys.stdin.readline().strip()
    for i in range(len(in_str)):
        tmp[9-int(in_str[i])] = '1'

    #2. lst배열에 위에서 변환한 이진수에 해당하는 십진수의 index에 1만큼 값을 더해줌. 
    lst[int("0b" + "".join(tmp[::-1]), 2)] +=1

#3. 1024개의 값중 존재하는 값만 계산하면 되므로 lst에서 index가 1이상인 값을 찾아서 cal_lst에 저장
cal_lst = []
for i in range(1024):
    if lst[i] !=0:
        #cal_lst에 저장할때는 [index, index에 값이 몇개나 있는지]
        cal_lst.append([i, lst[i]])

#4. 정답을 저장하기 위해 ans변수 선언
ans = 0
#5-1. cal_lst에서 자기 자신을 탐방하면서 
for i in range(len(cal_lst)):
    #5-2. 2개 이상의 값이 있다면 
    if cal_lst[i][1] > 1:
           #5-3.자기 자신을 or한 값에서도 K-문자열을 만들 수 있는 수가 나오므로
           if bin(cal_lst[i][0]).count('1') == K :
               #5-4. 위의 과정이 옳다면 cnt*(cnt-1)//2만큼 ans값에 포함해줌.
               #이는 다른것중 2개를 꺼내는 nC2과정과 동일
               ans += (cal_lst[i][1] * (cal_lst[i][1]-1)) //2
    #6-1. 자기 자신과의 계산을 고려한 후 자기를 제외한 나머지 값과 비교를 하는데
    for j in range(i+1, len(cal_lst)):
        #6-2. 자기 자신을 제외한 나머지 값과의 or연산에서 K-문자열을 만족한다면 
        if bin(cal_lst[i][0] | cal_lst[j][0]).count('1') == K:
            #6-3. 정답에 자기 자신의 갯수와 계산한 값의 갯수를 곱해서 정답에 더해준다
            ans += cal_lst[i][1] * cal_lst[j][1]
        
print(ans)