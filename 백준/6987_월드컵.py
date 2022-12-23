answer = []

for i in range(4):
    arr = list(map(int,input().split()))
    winLose=0
    dir = 0
    draw = 0
    cnt = 0
    for i in range(18):
        if i%3==0:
            winLose += arr[i]
            cnt += arr[i]
            if sum(arr[i:i+3]) > 5:
                cnt += 30
                break

        elif i%3==2:
            winLose -= arr[i]
            cnt += arr[i]
        else: #i%3 ==1  나머지가 1일때
            # print(i)
            cnt += arr[i]
            if arr[i] and dir == 0:
                draw += arr[i]
                dir = 1
            elif arr[i] and dir == 1:
                draw -= arr[i]
                dir = 0
    # print(winLose,draw)
    if cnt > 30:
        answer.append(0)
    elif winLose or draw:
        answer.append(0)
    else:
        answer.append(1)
    # print(winLose,draw)
print(*answer)