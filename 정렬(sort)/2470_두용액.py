import sys
n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))

left = 0
right = n-1

cnt = abs(lst[left] + lst[right])
ans = [lst[left], lst[right]]


while left < right:
    sum = lst[left]+lst[right]
  
    if abs(sum) < cnt:
        cnt = abs(sum)
        ans = [lst[left], lst[right]]
        if cnt == 0:
          break

    if sum < 0:
        left += 1
    else:
        right -= 1

print(*ans)