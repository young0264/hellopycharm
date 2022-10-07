t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    vrr = list(map(int, input().split()))
    max_vrr, cnt_vrr,flag = 0, 0,0

    for i in range(len(vrr) - 1):
        max_vrr = max(max_vrr,vrr[i])

    if max_vrr < vrr[-1]:
        print(0)
        continue

    sec = []
    for i in range(len(vrr)-1):
        if x % vrr[i] == 0:
            sec.append(x // vrr[i])
        else:
            sec.append((x // vrr[i]) + 1)
    min_sec = min(sec)
    #부스터 최대치 사용했을때 #x-y > 0
    if (x-y)%vrr[-1]==0 and (min_sec <= ((x-y)//vrr[-1])+1):
        print(-1)
        continue#continue
    elif (x-y)%vrr[-1]!=0 and (min_sec <= ((x-y)//vrr[-1]) +2 ):
        print(-1)
        continue
    print("sec", sec)


    mid = 0

    left, right = 0, y  #속도
    while left<right:
        my_sec = 0
        mid = (left+right)//2   #속도
        #my_sec 구하기
        if (x-mid)%vrr[-1] == 0: #부스터를 쓰고 남은거리를 현재속도로 가는데 걸리는 시간
            my_sec = 1+(x-mid)//vrr[-1]
        else:
            my_sec = 2+(x-mid)//vrr[-1]
        print(left,mid,right,my_sec,min_sec)

        if min_sec <= my_sec :
            left = mid+1
        else :
            right = mid - 1
        print(mid






