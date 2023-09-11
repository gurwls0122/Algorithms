#https://www.acmicpc.net/problem/16719
import sys
word = str(sys.stdin.readline().strip())
ans =[''] * len(word)

#재귀를 이용하여 풀이, 인자로는 현재 확인해야될 substr과 index를 정확한 위치에 넣어주기 위한 시작 위치 start
def recursion(substr, start):
    global ans

    #만약 substr이 비어있다면 멈춤
    if not substr:
        return
    
    #현재 substr중에서 가장 작은 알파벳을 찾은 후 index을 idx에 저장
    val = min(substr)
    idx = substr.index(val)

    #해당 index의 위치에 문자 저장후 출력
    ans[start+idx] = val
    print("".join(ans))

    #이후 가장 작은 문자 기준 오른쪽->왼쪽 순으로 재귀 반복
    recursion(substr[idx+1:], start+idx+1)
    recursion(substr[:idx], start)

if __name__ == "__main__":
    recursion(word, 0)
    