from collections import deque
#다음값에 들어갈때 스택의 -1번째값을 비교해줘야해
n = int(input())
arr = deque(map(int, input().split()))
brr = []
i = 1
while len(arr):
    if arr and i == arr[0]:  # and arr?
        i += 1
        arr.popleft()
    else:
        brr.append(arr.popleft())
    while len(brr) and brr[-1] == i:######표현식. 이게아니면 멈추는
        brr.pop()
        i += 1
if brr:
    print("Sad")
else: print("Nice")
