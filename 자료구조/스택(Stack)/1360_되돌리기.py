#https://www.acmicpc.net/problem/1360
import sys
N = int(sys.stdin.readline())

#입력을 저장해놓을 리스트
lst = []
#정답 str을 저장해놓을 변수
ans = ""

#먼저 입력을 lst에 저장해놓음
for _ in range(N):
    cmd, ch, time = map(str, sys.stdin.readline().strip().split())
    lst.append((cmd, ch, time))

#리스트를 뒤에서 부터 탐색하면서
while lst:
    cmd, ch, time = lst.pop()
    #만약 type이 나왔다면 정답 str에 해당 문자를 추가해줌
    if cmd == "type":
        ans = ch+ans
    #만약 undo가 나왔다면 해당하는 되돌려지는 명령어들은 실행이 되지 않을 것이므로
    #lst에 저장되어있는 명령어를 탐색하며 실행이 되지 않는 시간을 찾음.
    else:
        if lst ==[]:
            break
        else:
            while int(lst[-1][2]) >= int(time) - int(ch):
                lst.pop()
                #lst를 pop해준후 lst가 비어있게된다면 반복 중지.
                if lst == []:
                    break

print(ans)