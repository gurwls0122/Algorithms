#https://www.acmicpc.net/problem/1713
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

#사진틀에 몇번 학생의 틀이 걸려있는지 확인하기 위한 배열
#각 배열의 값은 해당 학생의 번호와 추천수를 튜플로 가진다.
frame = []
for i in range(K):
    #1. 사진틀에 자신의 번호가 있을 경우 추천수를 +1만큼 해줌
    flag = False
    for j in range(len(frame)):
        if flag:
            break
        
        if frame[j][0] == lst[i]:
            flag = True
            frame[j][1] +=1
            for k in range(j):
                if frame[k][1] < frame[j][1] or (frame[k][1]==frame[j][1] and frame[j][2]< frame[k][2]):
                    frame.insert(k, frame.pop(j))
                    break
    
    if flag == True:
        # print(frame)
        continue
    #2. 사진틀에 자리가 남아있을 경우, 추천수를 1로 새롭게 사진틀에 사진을 추가
    if len(frame)<N:
        frame.append([lst[i], 1, i])

    #3. 사진틀에 자리가 없는 경우, 추천수가 같은 것 중 오래된것을 버리고 새롭게 추가
    else:
        min_recom = frame[N-1][1]
        for idx in range(len(frame)):
            if frame[idx][1] <= min_recom:  
                frame.pop(idx)
                frame.append([lst[i], 1, i])
                break
    # print(frame)

frame.sort(key=lambda x: x[0])
for i in range(len(frame)):
    print(frame[i][0], end=" ")