#https://www.acmicpc.net/problem/20164
import sys
from itertools import combinations
#탐색을 위해 입력을 str형태로 받음.
N = sys.stdin.readline().strip()
max_cnt = 0
min_cnt = 10e9

def cal(n, cnt):
    global max_cnt, min_cnt
    # print(n)
    #각 자릿수의 숫자들을 보며 해당 자리의 숫자가 홀수일 경우 cnt + 1
    for i in range(len(n)):
        if int(n[i])%2 == 1:
            cnt+=1
        else:
            pass
    #숫자카드에 적혀있는 수가 세자리 일때
    if int(n) >=100:
        #combination으로 길이를 3등분 한 후에
        for i in combinations(range(0, len(n)-1),2):
            # 3등분 된 n을 slice하여 재귀로 자릿수가 한자리 남을때까지 진행
            cal(str(int(n[0:int(i[0])+1]) + int(n[int(i[0])+1 : int(i[1])+1]) + int(n[int(i[1])+1 : len(n)])), cnt)

    #숫자카드에 적혀있는 수가 두자리 일때
    elif int(n) >=10:
        cal(str(int(n[0]) + int(n[1])), cnt)

    # #숫자카드에 적혀있는 수가 한자리 일때
    else:
        max_cnt = max(max_cnt, cnt)
        min_cnt = min(min_cnt, cnt)

if __name__ == "__main__":
    cal(N, 0)
    print(min_cnt, max_cnt)
