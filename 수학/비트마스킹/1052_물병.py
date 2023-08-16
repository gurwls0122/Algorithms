#https://www.acmicpc.net/problem/1052
import sys
N, K = map(int, sys.stdin.readline().split())

def decimal2binary(num):
    #입력받은 수의 이진수 값을 역순으로 저장하는 배열
    binary = []
    
    while num>1:
        binary.append(num%2)
        num //=2
    binary.append(num)

    #이진수로 변환되었을 때 1의 갯수(새로 사야될 물병 확인용)
    count = 0
    for i in binary:
        if i==1:
            count+=1
    
    return binary, count

def binary2decimal(lst):
    ans = 0 
    for i in range(len(lst)):
        ans += 2**i * lst[i]
    return ans

if __name__ =="__main__":
    if N==1 or N<=K:
        print(0)
        exit()
    input_dec, count_one = decimal2binary(N)
    # print(input_dec, count_one)
    olim = 0
    ans_dec = []
    for i in range(len(input_dec)):
        if count_one+olim <=K:
            break
        if olim + input_dec[i] ==0:
            ans_dec.append(0)
        elif olim + input_dec[i] == 1:
            ans_dec.append(1)
            olim = 1
        elif olim + input_dec[i] == 2:
            ans_dec.append(0)
            olim = 1

        if input_dec[i] == 1:
            count_one-=1
        


    # print(ans_dec)
    print(binary2decimal(ans_dec))
    # print(input_dec)